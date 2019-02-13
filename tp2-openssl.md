# TP 2 : Autorités de certification et HTTPS

_François Lesueur ([francois.lesueur@insa-lyon.fr](mailto:francois.lesueur@insa-lyon.fr))_

Ce TP présente le modèle des autorités de certification et l'applique au protocole HTTPS. Il sera réalisé dans l'infrastructure MI-LXC, disponible [ici](https://github.com/flesueur/mi-lxc) (nécessite un Linux en root) ou dans la VM "tp-sec-debian" disponible en salle de TP (`/machines_virtuelles/secu_vms/master/tp-sec-debian.sh`, debian/debian et root/root). L'infrastructure déployée simule plusieurs postes dont un SI d'entreprise (firewall, DMZ, intranet, authentification centralisée, serveur de fichiers, quelques postes de travail interne), une machine d'attaquant (hacker), une machine domestique (home) et un "routeur" général (backbone).

* Pour une utilisation sur un poste personnel depuis le dépôt github, la procédure est expliquée dans le README.md (attention, le déploiement initial est long).
* Pour une utilisation dans la VM "tp-sec-debian", MI-LXC est déjà installé et l'infrastructure déployée. Il faut passer root puis aller dans le dossier `/root/mi-lxc`. Ensuite, `git pull` (pour récupérer les dernières modifications...) puis `./mi-lxc.py start`.

Dans ce TP, vous avez besoin de travailler dans plusieurs environnements simultanément (CA racine, CA intermédiaire, serveur HTTPS, client HTTPS, routeur). Les machines MI-LXC pertinentes sont `dmz` (CA et serveur HTTPS, nom DNS `dmz.target.virt`), `home` (client HTTPS), `backbone` (point d'attaque MitM). La CA devrait être gérée sur un poste isolé mais, cette notion d'isolation étant plutôt au programme de 5TC-SRS, vous pouvez utiliser la machine DMZ lors de ce TP. Pour vous connecter à ces machines :

* `./mi-lxc.py display home` : pour afficher le bureau de la machine home
* `./mi-lxc.py attach dmz` : pour obtenir un shell sur la machine dmz

Quelques exemples de bons tutoriaux pour le déploiement d'une CA :

* [PKI-Tutorial](https://pki-tutorial.readthedocs.io/en/latest/simple/index.html)
* [Jamielinux](https://jamielinux.com/docs/openssl-certificate-authority/)

Si, après avoir affiché à l'écran un document chiffré (par exemple avec la commande `cat`), votre terminal affiche de mauvais caractères, utilisez la combinaison de touches `Ctrl+v, Ctrl+o` pour retrouver un affichage fonctionnel (ou tapez `reset`).

Mise en place d'une CA à étage
==============================

En utilisant par exemple `openssl`, mettez en œuvre une CA avec paire de clés racine et certificat intermédiaire. Isolez bien les deux environnements dans deux dossiers distincts.


Installation d'un serveur HTTPS
===============================

Créez le matériel cryptographique pour mettre en place en place un serveur HTTPS. Configurez un serveur avec ce matériel, `apache httpd` par exemple.

Configurez également un client HTTPS de manière adaptée pour vous y connecter de manière sécurisée.

<!-- 
> Pour configurer et exécuter le serveur HTTPS, vous pouvez utiliser la VM "tp-sec-debian" disponible sur les postes du département. Pour la démarrer, il faut exécuter `/machines_virtuelles/secu_vms/master/tp-sec-debian.sh`. Les comptes disponible sont ensuite `root/root` et ̀`debian/debian`. Des redirections de ports sont configurées automatiquement, les ports 80 et 443 de la VM sont accessibles depuis un navigateur exécuté sur l'hôte par les URL `http://127.0.0.1:8080` et `https://127.0.0.1:8443`.
-->

Authentification mutuelle
=========================

Mettez en place une authentification des clients par le serveur au moyen de certificats clients.


Révocation
==========

Expérimentez les mécanismes de révocation disponibles (CRL, OCSP en ligne ou agrafé) pour révoquer le certificat serveur ainsi que les certificats clients.


Attaque Man-in-the-Middle
=========================

La machine backbone est sur le chemin des paquets. Vous pouvez voir les paquets routés avec `tcpdump -i eth1`. Pour récupérer les paquets adressés à la DMZ sur la machine backbone, vous pouvez par exemple utiliser `ifconfig eth1:0 192.168.1.2` sur backbone (cela attribue l'IP de la DMZ au backbone, qui conservera ainsi les paquets destinés à la DMZ).

Installez le nécessaire sur le backbone pour que la connexion vers `https://dmz.target.virt` se termine en fait sur le backbone (malicieux). Quelles en sont les limites ?

Une version un peu plus aboutie peut-être obtenue avec [sslstrip](https://moxie.org/software/sslstrip/), avec cependant les mêmes limites évidemment.

Bonus
=====

À l'aide des fonctions de base d'openssl (génération de clés et chiffrement), mettez en œuvre un protocole de cryptographie hybride pour échanger un message avec une autre personne de la salle.

<!-- pinning, hsts -->

