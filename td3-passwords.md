# TD 3 : Stockage et utilisation des mots de passe

_François Lesueur ([francois.lesueur@insa-lyon.fr](mailto:francois.lesueur@insa-lyon.fr))_

Ce TD présente l'univers de la vérification et de l'utilisation des mots de passe :

* Stockage et vérification côté serveur
* Stockage et utilisation côté client
* Risques associés

Dans l'ensemble des cas, nous souhaitons évaluer le cas d'une attaque qui exfiltre des fichiers de l'application (dont le fichier de la base de données ou le fichier `/etc/shadow` par exemple).

Notations
=========

* h(m) est le hash du message m
* Si K<sub>A</sub> est une clé symétrique, {m}<sub>K<sub>A</sub></sub> est le chiffré de m avec la clé K<sub>A</sub>, m = { {m}<sub>K<sub>A</sub></sub>}<sub>K<sub>A</sub></sub>
* Si Pub<sub>A</sub> et Priv<sub>A</sub> sont des clés asymétriques complémentaires publique/privée, {m}<sub>Pub<sub>A</sub></sub> est le chiffré de m avec la clé Pub<sub>A</sub> et m = { {m}<sub>Pub<sub>A</sub></sub>}<sub>Priv<sub>A</sub></sub>
* m signé avec la clé Priv<sub>A</sub> est noté m.{h(m)}<sub>Priv<sub>A</sub></sub>



Côté serveur
============

Considérons que nous avons la base d'utilisateurs suivante :

| Login | Password |
| - 	| - |
Alice 	| hujk15tr
Brice 	| jhjkh8!u
Charlie | jhjkh8!u
Didier 	| jhjkh8!u
Estelle | FdTycvO?
Florent | QazyfRT.
Gustave | JKhjjkde
Henri 	| Hhgfaaz9

Étudiez les schémas suivants :

* La base des mots de passe est stockée en clair ;
* La base des mots de passe est stockée chiffrée, en RSA par exemple ;
* La base des mots de passe est stockée sous forme de hash ;
* La base des mots de passe est stockée sous forme de hash salé ;
* La base des mots de passe est stockée sous forme de n itérations de hash salé (PBKDF2, comment choisir n, quelle évolution ?).

Pour chaque schéma, vous devez analyser :

* le processus et le coût de l'ajout d'un compte et de la vérification d'un mot de passe
* la gestion d'un utilisateur qui a perdu son mot de passe
* l'information révélée directement par la base de mots de passe
* le coût de cassage d'un mot de passe isolé
* le coût de cassage de la base entière




Côté client
===========

Un gestionnaire de mots de passe conserve une table liant un titre, un login et un mot de passe. Par exemple :

| Titre | Login | Password |
| - | - | - |
| CDiscount | Alice31 | hujk15tr |
| laposte.net | AliceLefur@laposte.net | jku78!io |
| CB | 4785 1547 4554 6657 | 7514 |

Considérons que l'utilisation de ce gestionnaire de mots de passe nécessite la saisie préalable d'un mot de passe maître, lors de l'ouverture.

Proposez la mise en œuvre d'un gestionnaire de mots de passe local puis d'un gestionnaire de mots de passe en ligne. Analysez les risques d'attaques par les différents acteurs (eux-mêmes ou suite à comprommission de leur infrastructure).


Pour approfondir
================

* [OWASP : Password Storage Cheat Sheet](https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet)
* [SOPHOS : Serious Security: How to store your users’ passwords safely](https://nakedsecurity.sophos.com/2013/11/20/serious-security-how-to-store-your-users-passwords-safely/)
