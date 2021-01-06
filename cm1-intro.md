# CM 1 : Introduction -- Notes de cours

_François Lesueur ([francois.lesueur@insa-lyon.fr](mailto:francois.lesueur@insa-lyon.fr), [@FLesueur](https://twitter.com/FLesueur))_

Brainstorming des mots-clés crypto et sécu des coms, classification
===========

Qu'est-ce que cela vous évoque ?

* Des protocoles (TLS, HTTPS, PGP, SMIME), des algos (RSA, AES, Diffie-Hellman)
* Des usages à QoS différentes (GSM, chat, VoIP, web)
* Des applications (Signal [coucou la NSA], Telegram [coucou le GRU]), TOR)
* Des propriétés (confidientialité, intégrité, non-répudiation, déni plausible, forward secrecy)

Qui en fait ? (crypto et plus généralement sécurité des coms)
=============

* Les mécréants bien sûr !
* Le e-commerce, le bancaire, les CB
* Les politiques (Telegram en France, cf plus haut). Certains pas assez (DNC hack)
* les lanceurs d'alerte
* les populations surveillées/opprimées/sous dictature (reconnue ou pas)

C'est une réaction à la surveillance des états/des attaquants, devenue trop facile. Le monde numérique a rendu l'observation d'une personne trop facile, disproportion entre le coût pour le surveillant et la quantité de données en sortie. Il y a clairement un _effet Snowden_

Histoire
========

De tous temps, depuis l'antiquité, il y a eu des communications secrètes sur des canaux non sûrs. L'historique est militaire évidemment, d'où la culture du secret sur ce que l'on sait faire/ce que l'on sait casser. Point qui sera approfondi lors de la séance 1 de travail perso.


Crypto et sécurité sw/hw
========================

Qu'est-ce que la sécurité des communications ?

* Sécurité du canal de transmission -> crypto
* Sécurité de l'implémentation crypto/son déploiement
* Sécurité du logiciel et du matériel

C'est en général les deux derniers éléments qui pourront être attaqués.

Attention, les communications ne sont pas que numériques, la crypto n'est qu'une partie de la solution. La sécurité des communications, plus globalement, relève de l'_OPSEC_, la sécurité opérationnelle, qui englobe toutes les méthodes allant du filtre écran dans le TGV (voire le non-travail dans le TGV) aux bonnes pratiques de mise à jour de logiciels en passant par la sécurité physique des terminaux nomades (pas altérés, pas laissés sans surveillance, etc.) L'utilisation de crypto forte n'est donc pas une garantie de non-observabilité (quitte à ce que cela demande des moyens qui peuvent aller à la pose de micros/caméras, comme depuis relativement longtemps).

De la même façon, l'absence/l'interdiction de crypto n'empêche pas d'avoir des communications secrètes. Autrement dit, en interdisant la crypto, les mécréants sauront toujours communiquer de manière (à peu près) sûre.

La crypto nous ramène, plus ou moins, à un niveau de sécurité des communications pré-monde numérique : écoute à grande échelle trop chère (?), écoute ciblée possible.

CSC
===

Objectifs CSC
-------------
__Déployer une architecture de communications sécurisées adaptée à un besoin :__

* Comprendre comment/pourquoi ça marche
* Comprendre les processus d'évolution
* Comprendre les hypothèses et les chaînes de confiance
* Percevoir les enjeux secrets étatiques et mondiaux
* Appréhender les risques restants



Plan CSC
--------

* Les enjeux éthiques
* Principes généraux d'usage
* Détour par la gestion des mots de passe
* Le problème de la gestion des clés
* Les protocoles cryptographiques pour la communication et l'authentification

Organisation du travail
-----------------------

* Préparation en autonomie
* Séance encadrée ensuite
