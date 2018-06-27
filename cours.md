# Cours de 4TC(A)-CSC : Cryptographie et Sécurité des Communications

_François Lesueur ([francois.lesueur@insa-lyon.fr](mailto:francois.lesueur@insa-lyon.fr), [@FLesueur](https://twitter.com/FLesueur))_,
_Walid Bechkit ([walid.bechkit@insa-lyon.fr](mailto:walid.bechkit@insa-lyon.fr))_


[Intro](#introduction-à-la-crypto) |
[Bases](#bases-de-la-crypto) |
[Maths](#maths-pour-la-crypto) |
[PKI](#infrastructures-à-clés-publiques-pki) |
[Enjeux](#enjeux-éthiques) |
[Biblio](#bibliographie)


Introduction à la crypto
========================

Pour cette séance, vous devez étudier l'histoire de la cryptographie et de son utilisation. Nous nous baserons pour cela sur l'article de Wikipedia qui propose un bon historique : [WikipediaFR](https://fr.wikipedia.org/wiki/Histoire_de_la_cryptologie)

N'oubliez pas d'aller remplir ensuite le QCM sur moodle !


Bases de la crypto
=================

Vous devez lire le cours de [Ghislaine Labouret](https://web.archive.org/web/20170516210655/http://www.hsc.fr/ressources/cours/crypto/crypto.pdf) <!-- http://www.hsc.fr/ressources/cours/crypto/crypto.pdf https://doc.lagout.org/security/Cryptographie%20.%20Algorithmes%20.%20Steganographie/HSC%20-%20Introduction%20a%20la%20cryptographie.pdf --> (jusqu'à la page 27/32). Vous y verrez les notions de cryptographie symétrique (ex AES), asymétrique (ex RSA), hash, chiffrement, signature ainsi que le problème de la distribution des clés. Ce cours est intéressant car bien construit mais assez ancien (2001). Les notions, principes et difficultés n'ont pas changé depuis, les algorithmes et tailles de clés si : cela vous donne une idée de l'évolution à attendre pendant les 10 prochaines années (hors découverte majeure). À vous de chercher quels sont les algorithmes souhaitables aujourd'hui. Pour les tailles de clés, le site [Key Length](http://www.keylength.com/) est très pratique.


La suite du travail est d'étudier le fonctionnement de RSA (sans entrer, pour l'instant, dans les fondements mathématiques), par exemple sur [Wikipedia](https://fr.wikipedia.org/wiki/Chiffrement_RSA). Prêtez une attention particulière à la génération des clés, aux mécanismes de chiffrement et déchiffrement.

Enfin, le programme [Bullrun](https://fr.wikipedia.org/wiki/Bullrun) donne un bon aperçu des forces et faiblesses de la cryptographie moderne : la partie mathématique est plutôt sûre, les attaques se concentrent sur l'usage (standardisation), le déploiement, l'implémentation, etc.

Ouverture (obligatoire): [La sélection de l'AES](https://videlalvaro.github.io/2014/03/you-dont-roll-your-own-crypto.html)

Ouverture (facultative):

* [L'histoire de Dual\_EC\_DRBG](https://en.wikipedia.org/wiki/Dual_EC_DRBG)
* [Listen up, FBI: Juniper code shows the problem with backdoors, _Fahmida Y. Rashid, InfoWorld_](http://www.infoworld.com/article/3018029/virtual-private-network/listen-up-fbi-juniper-code-shows-the-problem-with-backdoors.html)

Cette section sera conclue par le TD1.


Maths pour la crypto
====================

Cette partie de cours s'intéresse principalement aux fondements mathématiques des cryptosystèmes asymétriques basés sur la difficulté du problème de la factorisation des grands nombres entiers. Le cryptosystème RSA, sera en particulier, l’objet principal des deux séances.

Chacune des deux séances de TD et TP va se dérouler en deux phases:

* La première phase vise à comprendre la génération des clés RSA, la justification des choix des paramètres, le chiffrement, le déchiffrement, la preuve d’exactitude et l’évaluation du coût des opérations RSA. Le cryptosystème RSA sera mis en place en TP en utilisant Python 3 et une évaluation de temps d’exécution des opérations de chiffrement/déchiffrement en fonction des tailles de clés sera effectuée.

* La deuxième phase concernera le problème RSA et son lien avec la factorisation des grands nombres entiers. Quelques algorithmes de factorisation basiques seront proposées progressivement en TD et ensuite implémentés, évalués et comparés en TP.

Pour mieux suivre les différentes preuves et la conception de quelques algorithmes de factorisation, vous devez lire le cours de Marine Minier "Arithmétique pour la cryptographie" disponible [ici](http://perso.citi.insa-lyon.fr/mminier/images/Arithmetique_pour_Cryptographie_impression.pdf)  **jusqu'au slide 31** (vous pouvez sauter les slides 26 et 27 sur le théorème des restes chinois). Ce cours donne les bases d’arithmétiques nécessaires pour comprendre par la suite le cryptosystème RSA et les méthodes de factorisation qui seront traitées. Pour la Crible d'Ératosthène, lisez le principe sur [la page Wikipedia, section Algorithme](https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne). Pour la fonction indicatrice d'Euleur, lisez plus de détails sur la page [Wikipedia](https://fr.wikipedia.org/wiki/Indicatrice_d%27Euler).


Pour la première phase, relisez attentivement la [page Wikipédia]( https://fr.wikipedia.org/wiki/Chiffrement_RSA) expliquant RSA **jusqu’à la section « Asymétrie »**. Pour la partie problème RSA et factorisation, lisez la [page du problème RSA sur Wikipédia]( https://fr.wikipedia.org/wiki/Probl%C3%A8me_RSA) **jusqu’à la section « Lien avec la factorisation »**.

Ouverture :

Pour la partie factorisation, lisez le principe de l’algorithme p-1 de Pollard [Page Wikipédia, section principe]( https://fr.wikipedia.org/wiki/Algorithme_p-1_de_Pollard), le principe de l’algorithme de Pollard Rho [Page Wikipédia, section définition formelle]( https://fr.wikipedia.org/wiki/Algorithme_rho_de_Pollard) et le principe de l’algorithme de factorisation de Fermat [Page Wikipédia, sections intuition et méthode de base](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_factorisation_de_Fermat)


Le sujet de TD est disponible [ici](https://moodle.insa-lyon.fr/pluginfile.php/124789/mod_resource/content/2/TD_CSC.pdf)

Le sujet de TP est en cours de finalisation :)

<!--
Extrait du livre [Discrete Math for Computer Science Students, _Ken Bogart, Scot Drysdale, Cliff Stein_](https://web.archive.org/web/20170829125913/http://www.cse.iitd.ernet.in/~bagchi/courses/discrete-book/fullbook.pdf) ? -->

<!-- https://www.kth.se/social/files/557ec6b0f27654784e263d66/fullbook.pdf  ,  
www.cse.iitd.ernet.in/~bagchi/courses/discrete-book/fullbook.pdf -->

<!--
Ouverture (obligatoire) : [Exemple de crypto symétrique : AES](http://www.moserware.com/2009/09/stick-figure-guide-to-advanced.html)
-->

Infrastructures à clés publiques (PKI)
=======================================

Le rôle d'une PKI est de lier une clé publique à une identité (typiquement, à une chaîne de caractères intelligible comme une URL `www.acme.org` ou une adresse mail `brice@acme.org`). L'obtention de clés publiques est un service orthogonal au service de sécurité rendu par la cryptographie (ie, un même service, le mail chiffré et signé par exemple, peut-être rendu avec une approche type CA avec S/MIME ou une approche toile de confiance avec PGP).

Vous devez lire la [page anglaise de Wikipedia](https://en.wikipedia.org/wiki/Public_key_infrastructure) sur ce sujet, qui présente différentes formes de PKI (autorités de certifications, toile de confiance, SPKI, blockchain). Attention, la page française n'est pas assez détaillée.<!-- très différente et présente une vision réduites à l'approche CA, c'est uniquement la page anglaise qui fait référence pour ce cours. -->

Vous devez détailler chacune des différentes formes, avec une attention particulière pour les [CA](https://en.wikipedia.org/wiki/Certificate_authority) et le [Web of trust](https://en.wikipedia.org/wiki/Web_of_trust). La PKI DANE/TLSA est très bien décrite et positionnée dans cet [article](http://www.bortzmeyer.org/6698.html). Vous devez enfin lire les [Criticisms](https://en.wikipedia.org/wiki/Public_key_infrastructure#Criticism) de la page principale (et les détails de PKI security issues with X.509, Breach of Comodo CA, Breach of Diginotar).

Annexe (obligatoire). Pour comprendre DANE/TLSA qui repose sur DNSSEC, vous devez avoir compris le fonctionnement et les différents acteurs du système DNS (typiquement, notions de _registry_, _registrar_, gestion d'une zone et mécanisme de résolution récursif). Vous pouvez par exemple lire [Sebsauvage](http://sebsauvage.net/comprendre/dns/) jusque "Dans ce cas, ils sont à la fois registry et registrar.", [Bortzmeyer](http://www.bortzmeyer.org/files/cours-dns-cnam-PRINT.pdf) sections "Le protocole DNS" et "Gouvernance" et/ou d'autres ressources équivalentes.

Ouvertures (facultatives) :

* [SSL And The Future Of Authenticity, _Moxie Marlinspike (aka Mr. Signal)_](https://moxie.org/blog/ssl-and-the-future-of-authenticity/), ainsi que la [vidéo associée](https://media.defcon.org/DEF%20CON%2019/DEF%20CON%2019%20video%20and%20slides/DEF%20CON%2019%20Hacking%20Conference%20Presentation%20By%20-%20Moxie%20Marlinspike%20-%20SSL%20And%20The%20Future%20Of%20Authenticity%20-%20Video%20and%20Slides.m4v)
* [Quantifying Untrusted Symantec Certificates, _Arkadiy Tetelman_](https://arkadiyt.com/2018/02/04/quantifying-untrusted-symantec-certificates/)


<!-- moxie : https://www.youtube.com/watch?v=pDmj_xe7EIQ  https://www.youtube.com/watch?v=Z7Wl2FW2TcA  https://moxie.org/blog/ssl-and-the-future-of-authenticity/  https://media.defcon.org/DEF%20CON%2019/DEF%20CON%2019%20video%20and%20slides/DEF%20CON%2019%20Hacking%20Conference%20Presentation%20By%20-%20Moxie%20Marlinspike%20-%20SSL%20And%20The%20Future%20Of%20Authenticity%20-%20Video%20and%20Slides.m4v-->


Enjeux éthiques
===============

Pour conclure ce cours, nous allons nous intéresser aux enjeux de société liés à la cryptographie. Pour cela, vous devez consacrer le temps de préparation à lire des (parties de) documents suivants (si possible pas tous les mêmes, afin de diversifier les apports) :

* [WikipediaEN : Crypto wars](https://en.wikipedia.org/wiki/Crypto_Wars)
* [Listen up, FBI: Juniper code shows the problem with backdoors, _Fahmida Y. Rashid, InfoWorld_](https://www.infoworld.com/article/3018029/virtual-private-network/listen-up-fbi-juniper-code-shows-the-problem-with-backdoors.html)
* [The Risks of “Responsible Encryption”, _Riana Pfefferkorn_](https://cyberlaw.stanford.edu/files/publication/files/2018-02-05%20Technical%20Response%20to%20Rosenstein-Wray%20FINAL.pdf)
* [Keys Under Doormats: Mandating insecurity by requiring government access to all data and communications,_Abelson, Harold; Anderson, Ross; Bellovin, Steven M.; Benaloh, Josh; Blaze, Matt; Diffie, Whitfield; Gilmore, John; Green, Matthew; Landau, Susan; Neumann, Peter G.; Rivest, Ronald L.; Schiller, Jeffrey I.; Schneier, Bruce; Specter, Michael; Weitzner, Daniel J._](https://dspace.mit.edu/bitstream/handle/1721.1/97690/MIT-CSAIL-TR-2015-026.pdf?sequence=8)
* [The Moral Character of Cryptographic Work, _Phillip Rogaway_](http://web.cs.ucdavis.edu/~rogaway/papers/moral-fn.pdf)
* [Decrypting the encryption debate](https://www.nap.edu/catalog/25010/decrypting-the-encryption-debate-a-framework-for-decision-makers)
* [Conférence de clôture du SSTIC 2018, Patrick Pailloux, Directeur technique de la DGSE (vidéo, 1h)](https://www.sstic.org/2018/presentation/2018_cloture/)
<!-- https://www.wired.com/story/crypto-war-clear-encryption/ https://twitter.com/matthew_d_green/status/989222188287954945 https://blog.erratasec.com/2018/04/no-ray-ozzie-hasnt-solved-crypto.html  https://twitter.com/ErrataRob/status/989237973412732928 https://arstechnica.com/information-technology/2018/05/op-ed-ray-ozzies-crypto-proposal-a-dose-of-technical-reality/  -->

Cette liste n'est bien sûr pas exhaustive, toutes les suggestions d'ajout sont les bienvenues.

Un dernier questionnaire Moodle porte sur cette partie qui mènera à une discussion/débat lors de la séance de TD.


Bibliographie
=============

Livres :
* Histoire des codes secrets : De l'Égypte des Pharaons à l'ordinateur quantique, _Simon Singh_
* Architectures PKI et communications sécurisées, _DUMAS Jean-Guillaume, LAFOURCADE Pascal, REDON Patrick_
* Serious Cryptography, _Jean-Philippe Aumasson_

Films :
* Mr Robot
* The Imitation Game
* Citizenfour

![xkcd](https://imgs.xkcd.com/comics/security.png)

<a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/2.0/fr/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/2.0/fr/88x31.png" /></a><br />Ce(tte) œuvre est mise à disposition selon les termes de la <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/2.0/fr/">Licence Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 2.0 France</a>.
