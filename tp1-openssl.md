# TP 1 : Autorités de certification et HTTPS

_François Lesueur ([francois.lesueur@insa-lyon.fr](mailto:francois.lesueur@insa-lyon.fr))_

Ce TP présente le modèle des autorités de certification et l'applique au protocole HTTPS. Il sera réalisé dans l'infrastructure MI-LXC, disponible [ici](https://github.com/flesueur/mi-lxc) ou dans la VM "tp-sec-debian" disponible en salle de TP (`/machines_virtuelles/secu_vms/master/tp-sec-debian.sh`, root/root). L'infrastructure déployée simule plusieurs postes dont le SI de l'entreprise _target_ (routeur, serveur web, poste admin), le SI de l'autorité de certification _mica_, un AS d'attaquant _ecorp_ et quelques autres servant à l'intégration de l'ensemble.

* Pour une utilisation sur un poste personnel depuis le dépôt github, la procédure est expliquée dans le README.md.
* Pour une utilisation dans la VM "tp-sec-debian", MI-LXC est déjà installé et l'infrastructure déployée. Il faut passer root puis aller dans le dossier `/root/mi-lxc`. Ensuite, `./mi-lxc.py start`.

Vous pouvez afficher un plan de réseau avec `./mi-lxc.py print`.

Pour vous connecter à une machine :

* `./mi-lxc.py display isp-a-home` : pour afficher le bureau de la machine isp-a-home
* `./mi-lxc.py attach target-dmz` : pour obtenir un shell sur la machine target-dmz

L'objectif du TP est de permettre à la machine isp-a-home de naviguer de manière sécurisée sur le site `www.target.milxc` (hébergé sur la machine target-dmz).

Connexion en clair
==================

Depuis la machine isp-a-home, ouvrez un navigateur pour vous connecter à `http://www.target.milxc`. Dans un premier temps, nous allons attaquer depuis l'AS ecorp la communication en clair, non sécurisée, entre isp-a-home et target-dmz. Deux pistes peuvent être explorées :

* Attaque DNS qui, via le registrar, consisterait à altérer l'enregistrement DNS pour target.milxc dans la zone du TLD .milxc. Sur la machine milxc-ns :
	* Altération de `/etc/nsd/milxc.zone` puis `service nsd restart` (le DNS de ecorp est déjà configuré pour répondre aux requêtes pour target.milxc)
* Attaque BGP qui consisterait à dérouter les paquets à destination de l'AS target vers l'AS ecorp : 
	* Sur la machine ecorp-router : prendre une IP de l'AS target qui déclenchera l'annonce du réseau en BGP (`ifconfig eth1:0 10.100.1.1 netmask 255.255.255.0`)
	* Sur la machine ecorp-infra : prendre l'IP de `www.target.milxc` (`ifconfig eth0:0 10.100.1.2 netmask 255.255.255.0`)

Nous constatons ainsi le cas d'attaque que nous souhaitons détecter : un utilisateur sur isp-a-home qui, en tapant l'URL `www.target.milxc`, arrive en fait sur un autre service que celui attendu. Remettez le système en bon ordre de marche pour continuer.


Création d'une CA
=================

Pour sécuriser les communications vers `www.target.milxc`, nous allons créer, déployer et utiliser une CA. Cette CA sera hébergée dans l'AS mica et manipulée sur la machine mica-ca. Sur cette machine, en graphique, vous disposez d'un compte mail configuré `ca@mica.milxc`.

Quelques exemples de bons tutoriaux pour la création d'une CA sont proposés. Attention, dans cette partie, vous devez générer uniquement la CA (début du tuto, donc). La partie concernant la génération des clés du serveur web se fait dans la partie suivante, sur la machine target-admin.

* [PKI-Tutorial](https://pki-tutorial.readthedocs.io/en/latest/simple/index.html)
* [Jamielinux](https://jamielinux.com/docs/openssl-certificate-authority/)

Si, après avoir affiché à l'écran un document chiffré (par exemple avec la commande `cat`), votre terminal affiche de mauvais caractères, utilisez la combinaison de touches `Ctrl+v, Ctrl+o` pour retrouver un affichage fonctionnel (ou tapez `reset`).


Sécurisation du serveur target-dmz
==================================

Sur l'AS target, vous disposez :

* de la machine target-admin, graphique, sur laquelle est configuré un client mail pour l'adresse `admin@target.milxc` :
	* Génération de la paire de clés
	* Demande du certificat
	* Configuration du serveur web sur target-dmz via ssh

* du serveur target-dmz sur lequel il faut déployer du matériel cryptographique pour faire du HTTPS. Vous devrez notamment :
	* Activer le module TLS (HTTPS) pour apache2 : `a2enmod ssl`
	* Activer le site par défault servi en HTTPS : `a2ensite default-ssl.conf`
	* Redémarrer le serveur apache2 : `systemctl restart apache2`
	* Configurer le matériel cryptographique de ce nouveau site dans le fichier `/etc/apache2/sites-enabled/default-ssl.conf` (vous devez redémarrer le serveur apache2 après vos modifications)

Vous devrez également configurer le client Firefox sur isp-a-home de manière adaptée pour vous y connecter de manière sécurisée.


Risques lors de la création du certificat
=========================================

En reprenant les attaques du début, obtenez depuis ecorp un certificat bien signé par mica lié à l'URL `www.target.milxc`. Le serveur de mail de ecorp est configuré pour accepter des mails @target.milxc (s'ils arrivent sur ce serveur, ce qui n'est évidemment pas le cas en temps normal). L'adresse `admin@target.milxc` peut ainsi être relevée depuis la machine ecorp-hacker si le mail arrive sur le serveur ecorp-infra.

Validez la réussite en vous connectant depuis isp-a-home vers ce faux serveur, sans alerte de sécurité.

Authentification mutuelle
=========================

Mettez en place une authentification des clients par le serveur au moyen de certificats clients.


Révocation
==========

Expérimentez les mécanismes de révocation disponibles (CRL, OCSP en ligne ou agrafé) pour révoquer le certificat serveur ainsi que les certificats clients.




<!-- pinning, hsts -->

