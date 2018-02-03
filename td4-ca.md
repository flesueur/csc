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
4. Quelle est la procédure de vérification côté client web ? Quels sont les pré-requis ?


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


OCSP
----

OCSP (_Online Certificate Status Protocol_) permet à un client de vérifier en temps réel la validité d'un certificat auprès de la CA émettrice.

1. Cela résoud-il le risque que l'utilisation de CRL fait peser sur les CA ?
2. Avec l'agrafage OCSP (_stapling_), c'est le serveur web qui demande à la CA une preuve de validité valable 24h et la présente ensuite à ses clients. Cela résoud-il la surcharge de la CA ? Quelle différence par rapport à des certificats valables 24h ?

La révocation est un problème qui n'est toujours pas traité de manière satisfaisante...

Quand les problèmes commencent
==============================

Imaginez maintenant que l'une des autorités soit compromise (malveillante ou attaquée).

1. Quel impact pour les clients reconnaissant cette autorité ?
2. Quel impact pour un site dont le certificat est émis par une autre autorité ?
3. Comment y remédier dans le cas où c'est un certificat intermédiaire qui est compromis ? Dans le cas où c'est le certificat racine qui est compromis ?
