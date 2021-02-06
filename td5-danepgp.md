# TD 5 : DANE/PGP

_François Lesueur ([francois.lesueur@insa-lyon.fr](mailto:francois.lesueur@insa-lyon.fr))_

Ce TD présente les modèles de PKI "DANE" et "PGP/Web of trust". Comme pour le cas de la CA, ces PKI doivent permettre de valider la clé publique tierce obtenue pour une identité demandée.

Dans le mode distanciel, réfléchissez en _petits_ groupes (groupes de 2-4 ?) dans des salons de discussion spécifiques. Des éléments de réponse sont accessibles pour chaque question (en cliquant sur les questions) : réfléchissez sans ces éléments, puis regardez et intégrez ces éléments. L'enseignant fera le tour des groupes pour échanger sur les points nécessaires.


Notations
=========

* h(m) est le hash du message m
* Si Pub<sub>A</sub> et Priv<sub>A</sub> sont des clés asymétriques complémentaires publique/privée, {m}<sub>Pub<sub>A</sub></sub> est le chiffré de m avec la clé Pub<sub>A</sub> et m = { {m}<sub>Pub<sub>A</sub></sub>}<sub>Priv<sub>A</sub></sub>
* m signé avec la clé Priv<sub>A</sub> est noté m.{h(m)}<sub>Priv<sub>A</sub></sub>. *Nouveauté pour ce TD, maintenant qu'on a l'habitude, on pourra aussi noter m<sup>Priv<sub>A</sub></sup> cette signature*


DANE
====

Avec DANE, les certificats ou clés publiques sont stockés directement dans les zones DNS, qui doivent alors être signées avec DNSSEC.


Un peu de DNS
-------------

Allez vraiment lire la ressource donnée dans le cours [Bortzmeyer](http://www.bortzmeyer.org/files/cours-dns-cnam-PRINT.pdf), pages 3 à 9 et 18 à 19, ainsi que [Sebsauvage](http://sebsauvage.net/comprendre/dns/) jusque "Dans ce cas, ils sont à la fois registry et registrar.".

1. <details><summary>Qui héberge le contenu de la zone `'.fr'` ?</summary>L'AFNIC (un registry)</details>
2. <details><summary>Qui vend le service d'enregistrer un `'.fr'` ?</summary>OVH, Gandi, etc. (des registrars)</details>
3. <details><summary>Quelle chaîne commerciale/interactions d'un possesseur de nom de domaine à un registry ?</summary>INSA Lyon cliente d'un registrar (Gandi par exemple), ce registrar en interaction avec un grand nombre de registries (Afnic par exemple, un registry par extension/TLD proposé (plus ou moins)) </details>
3. <details><summary>Pour résoudre `www.insa-lyon.fr`, quels acteurs sont impliqués ?</summary>L'ICANN pour donner l'IP de `.fr`, l'AFNIC pour donner l'IP de `insa-lyon.fr`, l'INSA Lyon pour donner l'IP de `www.insa-lyon.fr`</details>


Un peu de DNSSEC (principe simplifié)
----------------

DNSSEC dispose d'une paire de clés racine, responsable de signer la zone racine `'.'`. Chaque niveau de hiérarchie (TLD, domaine, etc.) possède ensuite sa propre paire de clés (donc Pub<sub>fr.</sub>/Priv<sub>fr.</sub>, Pub<sub>insa-lyon.fr.</sub>/Priv<sub>insa-lyon.fr.</sub>, etc.), signée par la zone supérieure et utilisée pour signer la zone courante et les clés des zones descendantes directes.

1. <details><summary>Proposez un schéma clés/signatures allant jusqu'à la zone `'insa-lyon.fr'` contenant notamment une entrée pour `'www'` (quelle clés, qui signe qui, avec quelle clé, qui connaît quelle clé).</summary>Les clés impliquées : Pub<sub>.</sub>/Priv<sub>.</sub>, Pub<sub>fr.</sub>/Priv<sub>fr.</sub>, Pub<sub>insa-lyon.fr.</sub>/Priv<sub>insa-lyon.fr.</sub><br>Priv<sub>.</sub> est sous le contrôle de l'ICANN, Priv<sub>fr.</sub> est sous le contrôle de l'AFNIC, Priv<sub>insa-lyon.fr.</sub> sous le contrôle de l'INSA. Quand un insa-lyon.fr enregistre sa clé via son registrar (ex par GANDI), GANDI pousse cette clé vers l'AFNIC qui l'enregistre dans la zone .fr et la signe avec sa clé privée.<br><br>Et on a :<br><br>Pub<sub>fr.</sub><sup>.</sup> (signé par .)<br>Pub<sub>.insa-lyon.fr.</sub><sup>.fr.</sup>  (signé par .fr)<br>le champ A `www.insa-lyon.fr` signé par  Priv<sub>insa-lyon.fr.</sub></details>


2. <details><summary>La modification d'une zone demande-t-elle du travail supplémentaire aux zones supérieures ?</summary>Non, tout est cloisonné, la modification de l'IP de www.insa-lyon.fr demande juste à être re-signée par la clé de insa-lyon.fr. Besoin d'au-dessus uniquement pour changer la clé de insa-lyon.fr</details>

> Il s'agit ici du principe _très_ simplifié (et donc faux) de DNSSEC. Il y a en réalité 2 paires de clés à chaque instant pour chaque zone, la paire KSK (_Key Signing Key_) et ZSK (_Zone Signing Key_), des règles de roulement et un grand nombre de détails, DNSSEC est un protocole très compliqué. Ces spécificités ne sont cependant pas nécessaires pour comprendre le principe de DANE.


Mise en œuvre
-------------

1. <details><summary>Comment intégrer un enregistrement contenant une clé publique à la zone ?</summary>Un champ spécifique (TLSA au lieu de A pour une IP) contient une clé publique/un hash de clé publique</details>
2. <details><summary>Comment cet enregistrement est-il signé ?</summary>Par la clé privée de la zone</details>
3. <details><summary>Quelle est sa chaîne de confiance associée ?</summary>zone, TLD, root DNS</details>


Risques
-------

1. <details><summary>Quel impact si un attaquant obtient ma clé privée de zone (`'insa-lyon.fr'`) ?</summary>Compromission de ma zone pour tous les clients du monde</details>
2. <details><summary>Quel impact si ma zone parente est maveillante ou compromise (`'.fr'`) ?</summary>Compromission de ma zone pour tous les clients du monde</details>
3. <details><summary>Quel impact si une zone DNS non liée (par exemple `'.tv'` dans notre cas) est compromise ?</summary>Aucun impact sur ma zone (différent du modèle CA, les défaillances sont cloisonnées, 1 mauvais ne compromet pas l'ensemble du système)</details>



Gestion de la révocation
------------------------

1. <details><summary>En cas de vol de la clé privée du serveur web, comment révoquer son certificat ? Sous quel délai cela sera-t-il effectif ? Qui est impacté par la vérification de cette mise à jour ?</summary>Modif de la zone, resignage avec ma clé de zone. Délai : pas immédiat, pas de contrôle, temps de propagation DNS. Court (heures/jour) mais pas immédiat et sans contrôle. Contrairement aux CRL, c'est l'infra DNS qui supporte ce coût et il n'y a pas vraiment de surcoût (sauf si on réduit les TTL)</details>
2. <details><summary>En cas de vol de la clé privée de la zone, comment la révoquer ? Sous quel délai cela sera-t-il effectif ? Quel est le coût associé ?</summary>Révocation par la zone parente, qui est donc à impliquer. Délai de propagation aussi mais non maîtrisé (ie, le TTL de la zone .fr). Pas de coût particulier.</details>
3. <details><summary>En cas de vol de la clé privée racine, comment réagir ?</summary>Là, on a un gros problème, c'est l'ancre de confiance. De manière similaire à une CA compromise, il faut déployer une nouvelle clé chez les clients et donc mise à jour software des clients DNS pour intégrer une autre clé racine.</details>

> Le modèle et les risques associés sont donc assez différents. Mais, fondamentalement, c'est profiter d'un annuaire live et (presque) à jour déjà existant pour rendre ce service.

PGP
===

Avec PGP, chaque utilisateur est représenté par une paire de clés et peut être vu comme une mini autorité de certification.


Initialisation
--------------

Chaque utilisateur génère sa paire de clés publique/privée. La clé publique est classiquement téléversée sur un serveur afin de pouvoir être téléchargée par quiconque le souhaitant.

<details><summary>Quelles garanties peut-on avoir sur une clé simplement téléchargée pour l'adresse mail `'toto@acme.org'` ?</summary>Aucune évidemment, c'est comme la demander directement à la personne à travers ce medium de communication non sécurisé</details>


Reconnaissance de clés tierces
------------------------------

L'idée au centre de la toile de confiance (_web of trust_) est de signer les clés tierces que l'on a vérifiées (personnes que l'on connaît, _key-signing parties_). Chaque signature est décorée d'une valeur exprimant la confiance associée, par exemple :

* totale pour signifier que l'on fera aussi confiance aux clés signées par ce tiers ;
* partielle pour signifier que l'on ne fera _pas_ confiance aux clés signées par ce tiers.

L'agrégation de toutes ces signatures permet de modéliser le graphe de confiance.

Considérons ce graphe de confiance (chaque nom est l'alias d'une adresse mail) : ![pgp](td5-figures/pgp.png)


Chaque arc allant de A vers B a 2 valeurs :

* En label, le niveau de confiance de A sur l'identité de B (de 1-"je pense que c'est bien B à 3-"j'ai vérifié de mes yeux sa carte d'identité")
* En épaisseur de trait, le niveau de confiance de A pour que B vérifie bien les identités de ses contacts (de pointillé-"je pense qu'il n'est pas très attentif" à gras-"j'ai toute confiance dans la façon dont il évalue ses vérifications")

Évaluez la récupération de quelques clés et le score associé :

1. <details><summary>La clé de Henry par Jesse</summary>Le meilleur chemin est Jesse-Walter-Henry. Jesse a une confiance correcte en Walter pour certifier (la flèche moyenne), puis Henry a une forte confiance en l'identité qu'il associe à la clé de Henry. C'est un bon chemin et Jesse peut récupérer la clé de Henry ainsi avec une bonne confiance.</details>
2. <details><summary>La clé de Jesse par Saul</summary>Le meilleur chemin est Saul-Walter-Jesse. Saul a très peu confiance en Walter (flèche pointillée) pour vérifier les identités et donc le chemin ne valide pas. L'autre chemin Saul-Mike-Walter-Jesse bute également sur le chemin pointillé entre Mike et Walter</details>

> Il s'agit ainsi de parcourir le graphe, trouver les meilleurs chemins satisfaisant un seuil de confiance minimal. Plus le chemin est long plus la confiance va baisser (très vite), la présence de chemins multiples et disjoints peut ré-améliorer ce score. Il faut bien distinguer la confiance dans une identité (le nombre, ne dépend pas de l'attitude de la cible) de la confiance dans le comportement de la cible (l'épaisseur de la flèche). Chaque utilisateur a un rôle à jouer : bien faire son travail, et évaluer le travail qui sera fait par les autres. C'est difficile !

Composantes malicieuses
-----------------------

Imaginons qu'un attaquant crée un grand nombre d'identités et signe une clé pour l'adresse mail `'Henry@fbi.gov'`.

![pgp2](td5-figures/pgp2.png)

1. <details><summary>Évaluez la récupération de la clé de Henry par Jesse</summary>Aucun changement, la recherche ne peut pas rentrer dans la composante malicieuse qui est inatteignable pour Jesse</details>
2. <details><summary>Considérons maintenant que certaines personnes du graphe de confiance ne sont pas très regardantes sur leur validation et que Mike certifie William (score 3, gras). <img src="td5-figures/pgp3.png"> Évaluez la récupération de la clé de Henry par Saul</summary>Cette fois-ci, Saul va récupérer une mauvaise clé. Évidemment, il ne peut pas le savoir. Le chemin, pour cet exemple, est un peu long (Saul-Mike-William-Henry) et serait peut-être, en pratique, refusé, chaque saut dégradant le score. Mais c'est l'idée de ce risque.</details>
3. <details><summary>Quelles conclusions pouvons-nous en tirer sur la robustesse aux attaquants ?</summary>La robustesse aux attaquants est liée au bon usage de l'outil par chacun (ici, Skyler n'a pas bien évalué la confiance à accorder à Jack, mais Jesse est également en faute d'avoir lui-même accordé trop de confiance à Walter). L'usage est donc complexe, ce qui nuit à la sécurité finale.</details>


Révocation
----------

Comme pour toute PKI, il faut prévoir le cas de la perte ou du vol de clés privées.

1. <details><summary>Dans le cas où une clé privée serait compromise mais toujours connue, quelle réaction est possible ?</summary> on peut signer une révocation et l'enregistrer dans les serveurs de clés</details>
2. <details><summary>Dans le cas où une clé privée est perdue, quelle réaction est possible ?</summary> rien, plein de clés fantômes dans les serveurs de clé. Pire, si un attaquant la vole et nous l'efface, il l'a, peut l'utiliser légitimement, et nous on ne peut pas la révoquer...  À la création de clé, l'outil gpg prépare une révocation, qu'il demande de stocker à part et de manière pérenne pour pouvoir garantir qu'on pourra révoquer si besoin, mais plein de gens ne le font pas. Pas d'autorité supérieure qui peut révoquer des clés.</details>
