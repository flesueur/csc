# CM 3 : Wrap up -- Notes de cours

_François Lesueur ([francois.lesueur@insa-lyon.fr](mailto:francois.lesueur@insa-lyon.fr))_

Dans ce cours, nous assemblons les briques élémentaires vues auparavant (algorithmes de cryptographie) afin d'obtenir des propriétés de sécurité de plus haut niveau (protocoles cryptographiques).

Dessine-moi un protocole cryptographique
========================================

Schémas présentés :

* Cryptographie hybride, Diffie-Hellman, Perfect Forward Secrecy, _deniable encryption_ (déni plausible), _off-the-record messaging_ (deniable + PFS)
* Schéma d'authentification mutuelle (TLS, SSH), notions de négociation, _cipher suites_. On récupère en crypto (fort) le niveau de vérification originel (souvent plus faible, exemple mail)
* Needham–Schroeder, Kerberos, 3G/4G. Usage de cryptographie symétrique, pivot central pour faire communiquer tout le monde. 
* Signal, Telegram, Wire (_End-to-End/E2E encryption_) : PKI centralisée, même supply chain pour le logiciel de vérification. La sécurité repose quand même sur la confiance dans la PKI ainsi que sur le niveau de sécurité du SMS de vérification. L'asymétrique permet le E2E, mais finalement, une PKI centralisée est un pivot central pour tout le monde et rapproche le modèle de confiance de celui d'un opérateur cellulaire.

Quelques schémas utilisés :

![Diffie-Hellman](http://www.practicalnetworking.net/wp-content/uploads/2015/11/dh-revised-1024x751.png "Diffie-Hellman"){width=40%}

![TLS](http://rebecca.meritz.com/ggm15/handshake.png "TLS")

![Kerberos](https://upload.wikimedia.org/wikipedia/commons/a/a6/Kerberos-simple.svg "Kerberos")


Q&A
===
