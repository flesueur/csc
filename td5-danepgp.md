# TD 5 : DANE/PGP

_François Lesueur ([francois.lesueur@insa-lyon.fr](mailto:francois.lesueur@insa-lyon.fr), [@FLesueur](https://twitter.com/FLesueur) )_

Ce TD présente les modèles de PKI "DANE" et "PGP/Web of trust"

Notations
=========

* h(m) est le hash du message m
* Si K<sub>A</sub> est une clé symétrique, {m}<sub>K<sub>A</sub></sub> est le chiffré de m avec la clé K<sub>A</sub>, m = { {m}<sub>K<sub>A</sub></sub>}<sub>K<sub>A</sub></sub>
* Si Pub<sub>A</sub> et Priv<sub>A</sub> sont des clés asymétriques complémentaires publique/privée, {m}<sub>Pub<sub>A</sub></sub> est le chiffré de m avec la clé Pub<sub>A</sub> et m = { {m}<sub>Pub<sub>A</sub></sub>}<sub>Priv<sub>A</sub></sub>
* m signé avec la clé Priv<sub>A</sub> est noté m.{h(m)}<sub>Priv<sub>A</sub></sub>


DANE
====

Avec DANE, les certificats ou clés publiques sont stockés directement dans les zones DNS, qui doivent alors être signées avec DNSSEC.


Un peu de DNSSEC (principe simplifié)
----------------

DNSSEC dispose d'une paire de clés racine, responsable de signer la zone racine `'.'`. Chaque niveau de hiérarchie (TLD, domaine, etc.) possède ensuite sa propre paire de clés, signée par la zone supérieure et utilisée pour signer la zone courante et ses descendantes directes.

1. Proposez un schéma allant jusqu'à la zone `'insa-lyon.fr'` contenant notamment une entrée pour `'www'`.
2. La modification d'une zone demande-t-elle du travail supplémentaire aux zones supérieures ?

> Il s'agit ici du principe _très_ simplifié (et donc faux) de DNSSEC. Il y a en réalité 2 paires de clés à chaque instant pour chaque zone, la paire KSK (_Key Signing Key_) et ZSK (_Zone Signing Key_), des règles de roulement et un grand nombre de détails, DNSSEC est un protocole très compliqué. Ces spécificités ne sont cependant pas nécessaires pour comprendre le principe de DANE.


Mise en œuvre
-------------

1. Comment intégrer un enregistrement contenant une clé publique à la zone ?
2. Comment cet enregistrement est-il signé ?
3. Quelle est sa chaîne de confiance associée ?


Risques
-------

1. Quel impact si un attaquant obtient ma clé privée de zone ?
2. Quel impact si ma zone parente est maveillante ou compromise ?
3. Quel impact si une zone DNS non liée (par exemple `'.tv'` dans notre cas) est compromise ?


Gestion de la révocation
------------------------

1. En cas de vol de la clé privée du serveur web, comment révoquer son certificat ? Sous quel délai cela sera-t-il effectif ? Qui est impacté par la vérification de cette mise à jour ?
2. En cas de vol de la clé privée de la zone, comment la révoquer ? Sous quel délai cela sera-t-il effectif ? Quel est le coût associé ?
3. En cas de vol de la clé privée racine, comment réagir ?


PGP
===

Avec PGP, chaque utilisateur est représenté par une paire de clés et peut être vu comme une mini autorité de certification.


Initialisation
--------------

Chaque utilisateur génère sa paire de clés publique/privée. La clé publique est classiquement téléversée (sic) sur un serveur afin de pouvoir être téléchargée par quiconque le souhaitant.

Quelles garanties peut-on avoir sur une clé téléchargée pour l'adresse mail `'toto@acme.org'` ?


Reconnaissance de clés tierces
------------------------------

L'idée au centre de la toile de confiance (_web of trust_) est de signer les clés tierces que l'on a vérifiées (personnes que l'on connaît, _key-signing parties_). Chaque signature est décorée d'une valeur exprimant la confiance associée, par exemple :

* totale pour signifier que l'on fera aussi confiance aux clés signées par ce tiers ;
* partielle pour signifier que l'on ne fera _pas_ confiance aux clés signées par ce tiers.

L'agrégation de toutes ces signatures permet de modéliser le graphe de confiance.

1. Traçons ensemble ce graphe au tableau.
2. Évaluons la récupération de quelques clés par une personne donnée et le score associé.


Composantes malicieuses
-----------------------

Imaginons qu'un attaquant crée un grand nombre d'identités et signe une clé pour l'adresse mail `'toto@acme.org'`.

1. Ajoutez cela au graphe précédent.
2. Évaluons la récupération de la clé de `'toto@acme.org'` par une personne donnée et le score associé.
3. Considérons maintenant que certaines personnes du graphe de confiance ne sont pas très regardantes sur leur validation et faisons évoluer le graphe en conséquence, ré-évaluez la question précédente.
4. Quelles conclusions pouvons-nous en tirer sur la robustesse aux attaquants ?


Révocation
----------

Comme pour toute PKI, il faut prévoir le cas de la perte ou du vol de clés privées.

1. Dans le cas où une clé privée serait compromise mais toujours connue, quelle réaction est possible ?
2. Dans le cas où une clé privée est perdue, quelle réaction est possible ?
