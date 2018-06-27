# TP 2 : Autorités de certification et HTTPS

<!-- VPN avec auth mutuelle sur l'nfra LXC ? -->

_François Lesueur ([francois.lesueur@insa-lyon.fr](mailto:francois.lesueur@insa-lyon.fr))_

Ce TP présente le modèle des autorités de certification et l'applique au protocole HTTPS.

Si, après avoir affiché à l'écran un document chiffré (par exemple avec la commande `cat`), votre terminal affiche de mauvais caractères, utilisez la combinaison de touches `Ctrl+v, Ctrl+o` pour retrouver un affichage fonctionnel (ou tapez `reset`).

Dans ce TP, vous avez besoin de travailler dans plusieurs environnements simultanément (CA racine, CA intermédiaire, serveur HTTPS, client HTTPS), qui peuvent être simulés avec différentes machines (physiques ou virtuelles), différents containers docker ou au minimum des dossiers de travail clairement distincts.

Quelques exemples de bons tutoriaux :

* [PKI-Tutorial](https://pki-tutorial.readthedocs.io/en/latest/simple/index.html)
* [Jamielinux](https://jamielinux.com/docs/openssl-certificate-authority/)

<!-- TODO : dans l'infra LXC générique ? -->

Mise en place d'une CA à étage
==============================

En utilisant par exemple `openssl`, mettez en œuvre une CA avec paire de clés racine et certificat intermédiaire. Isolez bien les deux environnements.


Installation d'un serveur HTTPS
===============================

Depuis un environnement distinct, créez et obtenez le matériel cryptographique pour mettre en place en place un serveur HTTPS. Configurez un serveur avec ce matériel, `apache httpd` par exemple.

Configurez également un client HTTPS de manière adaptée pour vous y connecter de manière sécurisée.

> Pour configurer et exécuter le serveur HTTPS, vous pouvez utiliser la VM "tp-sec-debian" disponible sur les postes du département. Pour la démarrer, il faut exécuter `/machines_virtuelles/secu_vms/master/tp-sec-debian.sh`. Les comptes disponible sont ensuite `root/root` et ̀`debian/debian`. Des redirections de ports sont configurées automatiquement, les ports 80 et 443 de la VM sont accessibles depuis un navigateur exécuté sur l'hôte par les URL `http://127.0.0.1:8080` et `https://127.0.0.1:8443`.

Authentification mutuelle
=========================

Mettez en place une authentification des clients par le serveur au moyen de certificats clients.


Révocation
==========

Expérimentez les mécanismes de révocation disponibles (CRL, OCSP en ligne ou agrafé) pour révoquer le certificat serveur ainsi que les certificats clients.


Bonus
=====

À l'aide des fonctions de base d'openssl (génération de clés et chiffrement), mettez en œuvre un protocole de cryptographie hybride pour échanger un message avec une autre personne de la salle.

<!-- pinning, hsts -->

