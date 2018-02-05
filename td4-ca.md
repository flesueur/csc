# TD 4 : Autorités de certification

_François Lesueur ([francois.lesueur@insa-lyon.fr](mailto:francois.lesueur@insa-lyon.fr), [@FLesueur](https://twitter.com/FLesueur) )_

Ce TD présente le modèle de PKI "Autorités de certification", généralement noté CA (_Certification Authority_).

Notations
=========

* h(m) est le hash du message m
* Si K<sub>A</sub> est une clé symétrique, {m}<sub>K<sub>A</sub></sub> est le chiffré de m avec la clé K<sub>A</sub>, m = { {m}<sub>K<sub>A</sub></sub>}<sub>K<sub>A</sub></sub>
* Si Pub<sub>A</sub> et Priv<sub>A</sub> sont des clés asymétriques complémentaires publique/privée, {m}<sub>Pub<sub>A</sub></sub> est le chiffré de m avec la clé Pub<sub>A</sub> et m = { {m}<sub>Pub<sub>A</sub></sub>}<sub>Priv<sub>A</sub></sub>
* m signé avec la clé Priv<sub>A</sub> est noté m.{h(m)}<sub>Priv<sub>A</sub></sub>


Qu'est-ce qu'une CA ?
=====================

Une CA est une organisation cryptographiquement représentée par sa paire de clés Pub<sub>CA</sub> / Priv<sub>CA</sub>. Cette CA auto-signe son propre certificat.

1. Quelles informations contient son certificat ?
2. Quelle est sa forme signée, en utilisant la notation proposée ?


Qu'est-ce qu'un certificat de site HTTPS ?
==========================================

Un site HTTPS est cryptographiquement représenté par sa paire de clés Pub<sub>site</sub> / Priv<sub>site</sub>.

1. Quel est le problème si le serveur envoie tout simplement sa clé publique au début de l'échange ?
2. Quelles informations doit contenir son certificat ?
3. Quelle est sa forme signée, en utilisant la notation proposée ?
4. Quelle est la procédure de vérification côté client HTTPS ? Quels sont les pré-requis ?


Comment communiquer avec un voisin ?
====================================

Simulez maintenant une connexion vers le site de votre voisin, récupérez son certificat.

1. Pouvez-vous vérifier son certificat ?
2. Expliquez comment récupérer de manière adaptée les données qu'il vous manque.
3. Dans le cas de HTTPS, avec une multitude de CA (87 organisations, 166 certificats sur l'installation testée), comment cela est-il géré ?


Organisation d'une CA à étages
==============================

Pour limiter les risques et impacts d'une compromission, les CA emploient plusieurs clés de niveaux de sensibilité différents. Typiquement, un certificat racine avec une durée de vie longue (30 ans par exemple) est intégré aux navigateurs. La clé privée associée à ce certificat est stockée hors-ligne et est utilisée, chaque année, pour signer un certificat intermédiaire avec une durée de vie plus courte (1 an). C'est ensuite ce certificat intermédiaire qui est utilisé au quotidien. Formalisez cette organisation (matériel côté CA, matériel côté site, matériel côté client).


Révocation
==========

La certification est un processus _hors-ligne_, c'est-à-dire qu'une fois émis, un certificat reste valide jusqu'à une date fixée lors de la signature (typiquement en années). Il ne s'agit pas d'une validation interactive valable à l'instant de la requête HTTP.

Dans ses processus, une CA doit donc permettre de révoquer des certificats lorsqu'un site se fait voler sa clé privée.

CRL
---

La CRL (_Certificate Revocation List_) est une liste des certificats révoqués, émise et tenue à jour par la CA.

1. Quelle forme peut-elle avoir ?
2. Expliquez en quoi l'utilisation de CRL va à l'encontre de l'approche hors-ligne (non interactive) et quel risque cela pose pour la CA.
3. Que faire en cas de CRL non à jour et de CA non disponible pour mettre à jour ?


OCSP
----

OCSP (_Online Certificate Status Protocol_) permet à un client de vérifier en temps réel la validité d'un certificat auprès de la CA émettrice.

1. Cela résoud-il le risque que l'utilisation de CRL fait peser sur les CA ?
2. Avec l'agrafage OCSP (_stapling_), c'est le serveur web qui demande à la CA une preuve de validité valable 24h et la présente ensuite à ses clients. Cela résoud-il la surcharge de la CA ? Quelle différence par rapport à des certificats valables 24h ?
3. Que faire en cas d'absence d'agrafage OCSP ?

La révocation est un problème qui n'est toujours pas traité de manière satisfaisante et uniforme...

Quand les problèmes commencent
==============================

Imaginez maintenant que l'une des autorités soit compromise (malveillante ou attaquée).

1. Quel impact pour les clients reconnaissant cette autorité ?
2. Quel impact pour un site dont le certificat est émis par une autre autorité ?
3. Comment y remédier dans le cas où c'est un certificat intermédiaire qui est compromis ? Dans le cas où c'est le certificat racine qui est compromis ?


Ouverture : création et déploiement automatisés
===============================================

Pour du déploiement rapide, la création de certificats peut être automatisée. C'est par exemple le cas du protocole ACME proposé et utilisé par _Let's Encrypt_ ou d'approches plus ou moins artisanales pour du déploiement continu en approche _DevOps_ (le protocole ACME peut aussi être utilisé dans ce cas là).

L'objectif des certificats est d'éviter les attaques de type _Man-in-the-Middle_. Pour cela, un certificat valide la possession d'un nom hôte vis-à-vis de la CA émettrice. Nous pouvons imaginer un certain nombre de possibilités pour vérifier cette possession lors de la signature :

* une preuve administrative envoyée à la CA (non utilisé pour les certificats classiques, nécessaire pour les "EV") ;
* la réception d'un mail contenant un secret envoyé sur le domaine visé par la CA (approche classique des CA, en sachant que le mail n'est pas un protocole de communication sécurisé) ;
* la vérification que plusieurs chemins de communication disjoints existent de manière identique et que, donc, il n'y a pas de MitM entre la cible et la CA lors de cette étape (approche ACME, sous l'hypothèse que le MitM n'est pas en bout de communication côté client).

1. Schématisez un processus de vérification du type du protocole ACME (hôte cible, serveurs de vérification, clés de la CA, messages échangés).
2. Proposez un workflow de déploiement continu intégrant la création d'un certificat avec une CA locale puis avec _Let's Encrypt_.
