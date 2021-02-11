# TP 1 : Autorités de certification et HTTPS

_François Lesueur ([francois.lesueur@insa-lyon.fr](mailto:francois.lesueur@insa-lyon.fr))_

<!-- TODO
Une CA préconfigurée (et donc dans le TP, il faut l'opérer) et déjà reconnue par les browsers
Un certificat de nouvelle CA diffusé dans une maj de browser
Passer à du ACME avec Boulder/certbot
Faire un début style TD : après les premières attaques, une partie feuille avec récap au tableau sur tout le setup qu'il faudra mettre en place avec openssl
Mieux clarifier/séparer les différents rôles à jouer
BGP : https://radar.qrator.net/blog/as1221-hijacking-266asns
-->

Ce TP présente le modèle des autorités de certification et l'applique au protocole HTTPS. Il sera réalisé dans la VM VirtualBox MI-LXC disponible [ici](https://filesender.renater.fr/?s=download&token=42897b0b-604d-499d-8cff-30bbf9c3f586)<!-- (https://mi-lxc.citi-lab.fr/data/milxc-debian-amd64-1.3.0.ova)-->. Comme expliqué dans la [vidéo tuto](https://videos.insa-lyon.net/videos/?video=MEDIA200924154800396) (**à regarder avant ou au début de TP !**, la vidéo décrit l'installation, la prise en main et le lancement mais attention la fin de la vidéo décrit des machines et interactions liées à un autre TP de 5TC-SRS), avant de lancer la VM, il peut être nécessaire de diminuer la RAM allouée. Par défaut, la VM a 3GO : si vous avez 4GO sur votre machine physique, il vaut mieux diminuer à 2GO, voire 1.5GO pour la VM (la VM devrait fonctionner de manière correcte toujours).

L'infrastructure déployée simule plusieurs postes dont le SI de l'entreprise _target_ (routeur, serveur web, poste admin), le SI de l'autorité de certification _mica_, un AS d'attaquant _ecorp_ et quelques autres servant à l'intégration de l'ensemble.

> Pour les curieux, le code de MI-LXC, qui sert à générer cette VM automatiquement, est disponible avec une procédure d'installation documentée [ici](https://github.com/flesueur/mi-lxc)


Vous devez vous connecter à la VM en root/root. MI-LXC est déjà installé et l'infrastructure déployée, il faut avec un terminal aller dans le dossier `/root/mi-lxc`. Pour démarrer l'infrastructure, tapez `./mi-lxc.py start`.

Vous pouvez afficher un plan de réseau avec `./mi-lxc.py print`.

Pour vous connecter à une machine :

* `./mi-lxc.py display isp-a-home` : pour afficher le bureau de la machine isp-a-home qui vous servira de navigateur web dans ce TP (en tant qu'utilisateur debian)
* `./mi-lxc.py attach target-dmz` : pour obtenir un shell sur la machine target-dmz qui héberge le serveur web à sécuriser (en tant qu'utilisateur root)

Toutes les machines ont les deux comptes suivants : debian/debian et root/root (login/mot de passe).

**L'objectif du TP est de permettre à la machine isp-a-home de naviguer de manière sécurisée sur le site `www.target.milxc` (hébergé sur la machine target-dmz).**

> Si la souris reste bloquée dans une fenêtre virtuelle, appuyez sur CTRL+SHIFT pour la libérer.

> Dans la VM et sur les machines MI-LXC, vous pouvez installer des logiciels supplémentaires. Par défaut, vous avez mousepad pour éditer des fichiers de manière graphique. La VM peut être affichée en plein écran. Si cela ne fonctionne pas, il faut parfois changer la taille de fenêtre manuellement, en tirant dans l'angle inférieur droit, pour que VirtualBox détecte que le redimensionnement automatique est disponible. Il y a une case adéquate (taille d'écran automatique) dans le menu écran qui doit être cochée. Si rien ne marche, c'est parfois en redémarrant la VM que cela peut se déclencher. Mais il *faut* la VM en plein écran.


Connexion en clair
==================

Depuis la machine isp-a-home, ouvrez un navigateur pour vous connecter à `http://www.target.milxc`. Vous accédez à une page Dokuwiki, qui est bien la page attendue.

Nous allons maintenant attaquer depuis l'AS ecorp cette communication en clair, non sécurisée, entre isp-a-home et target-dmz. L'objectif est que le navigateur, lorsqu'il souhaite se connecter à l'URL `http://www.target.milxc`, arrive en fait sur la machine ecorp-infra. Deux pistes peuvent être explorées :

* Attaque DNS qui, via le registrar, consisterait à altérer l'enregistrement DNS pour target.milxc dans la zone du TLD .milxc. Sur la machine milxc-ns :
	* Altération de `/etc/nsd/milxc.zone` pour diriger les requêtes DNS pour `target.milxc` vers 100.81.0.2 (appartenant à ecorp)
	* Puis `service nsd restart` (le DNS de ecorp est déjà configuré pour répondre aux requêtes pour target.milxc)
* Attaque BGP qui consisterait à dérouter les paquets à destination de l'AS target vers l'AS ecorp (un [exemple de BGP hijacking réel en 2020](https://radar.qrator.net/blog/as1221-hijacking-266asns)) :
	* Sur la machine ecorp-router : prendre une IP de l'AS target qui déclenchera l'annonce du réseau en BGP (`ifconfig eth1:0 100.80.1.1 netmask 255.255.255.0`)
	* Sur la machine ecorp-infra : prendre l'IP de `www.target.milxc` (`ifconfig eth0:0 100.80.1.2 netmask 255.255.255.0`)

Nous constatons ainsi le cas d'attaque que nous souhaitons détecter : un utilisateur sur isp-a-home qui, en tapant l'URL `www.target.milxc`, arrive en fait sur un autre service que celui attendu. Remettez le système en bon ordre de marche pour continuer (pour DNS, remettre la bonne IP 100.80.1.2 ; pour BGP, désactivez l'interface eth1:0 sur ecorp-router `ifconfig eth1:0 down`).


Création d'une CA
=================

Pour sécuriser les communications vers `www.target.milxc`, nous allons créer, déployer et utiliser une CA. Cette CA sera hébergée dans l'AS mica et manipulée sur la machine mica-infra (son nom DNS dans l'infra sera `www.mica.milxc`). Nous utiliserons le protocole ACME (celui de Let's Encrypt) pour l'opération de la CA (challenges, émission des certificats) via la suite d'outils de Smallstep.

Dans un premier temps, il faut initialiser une nouvelle CA en tant que root (création d'une paire de clés, d'un certificat racine, etc.) ([doc](https://smallstep.com/docs/step-ca/getting-started)) :

	# step ca init                  <- le # dénote une commande shell à taper en root
	# step-ca .step/config/ca.json  <- démarre le serveur de CA
	# step ca root root.crt         <- ceci extrait le certificat racine vers le fichier root.crt

> La commande step-ca est bloquante, soit vous la mettez en arrière plan avec Ctrl+z puis `bg`, soit vous ouvrez ensuite un autre terminal

Dans un second temps, il faut activer le protocole ACME pour cette CA ([doc](https://smallstep.com/docs/tutorials/acme-challenge), le protocole ACME est responsable des défis/réponse pour la génération automatique des certificats) <!-- (https://smallstep.com/blog/private-acme-server/)-->

	# step ca provisioner add acme --type ACME

Rendez le certificat racine accessible au téléchargement, par exemple en le copiant (avec les bons droits) vers `/var/www/html` (il sera ainsi accessible depuis toutes les autres machines par l'URL `http://www.mica.milxc/root.crt`).

> Si, après avoir affiché à l'écran un document chiffré (par exemple avec la commande `cat`), votre terminal affiche de mauvais caractères, utilisez la combinaison de touches `Ctrl+v, Ctrl+o` pour retrouver un affichage fonctionnel (ou tapez `reset`).

> Pour reprendre la configuration à 0, il faut supprimer le dossier `/root/.step` sur la machine mica-infra


Intégration de la CA à l'écosystème HTTPS
=========================================

Pour que la CA soit opérationnelle, il faut qu'elle soit reconnue par les clients HTTPS, ie, les navigateurs web (Firefox ici). Cette reconnaissance, dans le cas d'une CA globale, passe par l'intégration du certificat racine dans le magasin de certificats fourni avec le navigateur, donc par l'éditeur de ce navigateur.

> En entreprise, on rencontre souvent une CA locale qui est ajoutée localement au magasin de certificats. Dans ce TP, nous étudions le fonctionnement général de HTTPS global à travers le monde et non un déploiement à l'échelle locale.

Vous devez pour cela :
* Passer le filtre des éditeurs de navigateurs et les convaincre de reconnaître votre CA. Il s'agit bien évidemment d'une opération complexe, longue, coûteuse et rare. Ici, nous la simulerons chez l'éditeur de navigateur Gozilla. La machine `gozilla-infra` peut intégrer un certificat préalablement téléchargé au trousseau par défaut avec la commande `addcatofox.sh <certificate>` . Une fois cette commande exécutée, la distribution du navigateur (ou de ses mises à jour) intégrera ce nouveau certificat.
* Déclencher la mise à jour du navigateur par le client, en exécutant `updatefox.sh` en tant que root sur la machine `isp-a-home`

La nouvelle CA est ainsi devenue une CA par défaut, reconnue globalement. Vérifiez, après avoir redémarré Firefox, que vous la retrouvez bien dans le magasin de certiticats de Firefox.


Certification du serveur target-dmz
==================================

Sur l'AS target, vous disposez du serveur target-dmz sur lequel il faut déployer du matériel cryptographique pour faire du HTTPS. Vous devrez notamment :

* Générer une paire de clés et obtenir le certificat correspondant depuis la CA MICA (les clés arrivent dans `/etc/letsencrypt/live/www.target.milxc/`) :

		# service apache2 stop    <- on libère le port 80 nécessaire à certbot
		# certbot certonly -n --standalone -d www.target.milxc \
			--server https://www.mica.milxc/acme/acme/directory
		# service apache2 start

* Configurer le matériel cryptographique de ce nouveau site dans le fichier `/etc/apache2/sites-enabled/default-ssl.conf` (vous devrez utiliser la chaîne complète de certificats depuis la racine, c'est-à-dire `fullchain.pem`, et la clé `privkey.pem`).
* Vous devez redémarrer le serveur apache2 après vos modifications : `systemctl restart apache2`

Connectez-vous maintenant en HTTPS depuis `isp-a-home` (si vous aviez ajouté une exception de sécurité à un moment du TP, retirez-la avant). Tout doit se dérouler sans alerte, visualisez le certificat reçu. (Vous arrivez sur une page par défaut, le dokuwiki est accessible à l'URL `https://www.target.milxc/dokuwiki/`)

<!-- ou apt install python3-certbot-apache puis un --apache au lieu du --standalone -->

Attaques sur un serveur HTTPS
=============================

Attaque sur la connexion au serveur
-----------------------------------

Refaites l'attaque du début (DNS ou BGP) et vérifiez que la connexion depuis isp-a-home, lorsqu'elle est routée vers le serveur attaquant, génère bien une alerte de sécurité.

<!-- il faudrait un certificat plus joli -->

Quelle est d'habitude votre réaction face à ce genre d'alerte ? Que pouvons nous en conclure sur la protection et le risque restant avec HTTPS ?


Attaque lors de la création du certificat
-------------------------------

En reprenant les attaques du début, obtenez depuis ecorp-infra un certificat bien signé par MICA lié à l'URL `www.target.milxc`. Ces attaques DNS/BGP vont vous permettre de vous faire passer pour Target auprès de mica, lors de la phase de création du certificat.

Validez la réussite en vous connectant depuis isp-a-home vers ce faux serveur, maintenant sans alerte de sécurité.


Bonus : Authentification mutuelle
=========================

Mettez en place une authentification des clients par le serveur au moyen de certificats clients.

Attention vous ne pourrez pas le faire avec ACME (les certificats clients ne correspondent pas à des noms d'hôtes et ne sont donc pas validables avec ACME). La partie de doc nécessaire est [ici](https://smallstep.com/onboarding/client-create-certificate)

<!--
Bonus : Révocation
==========

Expérimentez les mécanismes de révocation disponibles (CRL, OCSP en ligne ou agrafé) pour révoquer le certificat serveur ainsi que les certificats clients.
-->



<!-- pinning, hsts -->
