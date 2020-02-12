Questionnaire 4TC-CSC
=====================

Les questions sont organisées en 3 niveaux :

* Niveau 1 : C'est une question simple, la réponse est disponible à côté. La préparation du cours doit permettre d'y répondre directement.
* Niveau 2 : C'est une question moyenne, des éléments de réponse seulement sont fournis. La compréhension du cours doit permettre de répondre.
* Niveau 3 : C'est une question compliquée, sans correction unique, à discuter de vive voix.

Les réponses, quand disponibles, sont accessibles en cliquant sur le texte de la question.

Niveau 1
========

Intro
-----

<details> 
<summary>La cryptographie est-elle un moyen infaillible et suffisant pour communiquer de manière sécurisée ?</summary>
Non
</details>

<details> 
  <summary>Jules César utilisait-il un chiffrement basé sur l'exponentiation modulaire ? </summary>
   Non
</details>

<details> 
<summary>Enigma était utilisée pour communiquer entre les Alliés ?</summary>
Non
</details>

<details> 
<summary>Les usages civils de la cryptographie ont-ils toujours et partout été très libres ?</summary>
Pas partout, pas toujours
</details>






Bases de la crypto
------------------

<details>
<summary>Combien y'a-t-il de clés possibles en chiffrement par décalage (utilisé par le chiffre de César) ?</summary>
26
</details>

<details>
<summary>Enigma était-il un système de cryptographie symétrique ou asymétrique ?</summary>
Symétrique
</details>

<details>
<summary>Crypter signifie</summary>
Rien, le terme n'existe pas
</details>

<details>
<summary>En crypto symétrique, combien y a-t-il de clés pour 2 interlocuteurs ? Pour 4 interlocuteurs communiquant tous par paire ? </summary>
Une unique clé connue des 2 interlocuteurs - 8 clés
</details>

<details>
<summary>En crypto asymétrique, combien y a-t-il de clés pour 2 interlocuteurs ? </summary>
Une paire de clés par interlocuteur (4 clés pour 2 interlocuteurs)
</details>

<details>
<summary>Pour faire une signature non répudiable, faut-il de la crypto symétrique ou asymétrique ?</summary>
asymétrique
</details>

<details>
<summary>Une fonction de hachage est-elle à sens unique, bijective, inversible ou produit des sorties de taille variable ?</summary>
à sens unique
</details>

<details>
<summary>Quelle type de crypto (symétrique ou asymétrique) est aujourd'hui la plus rapide ?</summary>
symétrique
</details>

<details>
<summary>Selon l'ANSSI, quelle est la taille de clé à utiliser pour du RSA sûr jusqu'en 2025 ?</summary>
2048 bits
</details>

<details>
<summary>Dans la stratégie de la NSA pour casser les chiffrements (Bullrun), quels sont les axes de travail ?</summary>
Wikipedia :
<ol>
<li> des mesures pour s'assurer le contrôle sur l'établissement de normes américaines et internationales de chiffrement (NIST, normes ISO),</li>
<li> la collaboration avec des entreprises technologiques pour intégrer — dès la conception — des portes dérobées dans leurs solutions de chiffrement (logiciels ou puces électroniques),</li>
<li> la collaboration avec des fournisseurs de services Internet pour récupérer des certificats de chiffrement,</li>
<li> l'investissement dans des ordinateurs à hautes performances,</li>
<li> voire des cyberattaques ou l'espionnage des sociétés pour leur voler leurs clés numériques.</li>
</ol>
</details>

<details>
<summary>Quel algo a gagné la compétition AES ?</summary>
Rijndael
</details>



PKI
---

<details>
<summary>Qu'est-ce qu'une PKI ?
<ol>
	<li> Un système permettant d'associer une clé publique à une identité</li>
	<li> Un synonyme d'autorité de certification</li>
	<li> Un synonyme de toile de confiance</li>
	<li> Un serveur dédié à la récupération de clés privées</li>
</ol></summary>
Un système permettant d'associer une clé publique à une identité
</details>

<details>
<summary>Quelle garantie nous offre a priori une PKI ?
<ol>
	<li> Que la communication pourra être confidentielle et intègre</li>
	<li> Que ma machine ne sera pas compromise lors de la communication</li>
	<li> Que le serveur auquel je vais me connecter est bien celui qu'il prétend être</li>
	<li> Que le serveur auquel je vais me connecter n'est pas compromis</li>
</ol></summary>
1 et 3
</details>

<details>
<summary>En l'absence de PKI, comment établir une communication sécurisée sans connaissance préalablement partagée avec mon interlocuteur ?</summary>
Je ne peux pas
</details>




<details>
<summary>En général, comment sont validées les demandes de certificats par les CA ?
<ol>
	<li> Par email</li>
	<li> Par courrier postal</li>
	<li> En personne</li>
	<li> Par un formulaire administratif géré par chaque état</li>
</ol>
</summary>
Par email
</details>

<details>
<summary>Le marché des CA est opéré par des entreprises privées, des administrations publiques, des ONG et associations ou les auteurs de navigateurs web ?</summary>

Des entreprises privées
</details>

<details>
<summary>Dans la toile de confiance :
<ol>
	<li> Il y a un point central</li>
	<li> Chaque participant a un rôle équivalent</li>
	<li> Chacun choisit explicitement à qui il fait confiance</li>
	<li> Le fonctionnement est simple et automatique</li>
</ol>
</summary>
2 et 3
</details>

<details>
<summary>Du point de vue de l'utilisateur final côté client web, quelle PKI entre CA et PGP demande le moins d'expertise/de travail ?</summary>
CA
</details>

<details>
<summary>Avec DANE, quel sont les points de confiance les plus importants ?
<ol>
	<li> La racine DNS ?</li>
	<li> Les registrars ?</li>
	<li> Les autorités de certification ?</li>
	<li> Les utilisateurs du système ?</li>
</ol>
</summary>
La racine DNS et les registrars
</details>


Niveau 2
========


Q1 - Vous héritez de la maintenance d'une vieille application web dans laquelle les mots de passe des utilisateurs sont stockés sous forme de hash MD5. Vous décidez d'améliorer ce point.
* <details><summary>Pourquoi ce point pose-t-il problème ? Face à quel genre d'attaque ?</summary>hash faible, attaques par énumération/dictionnaire si vol de la base</details>
* <details><summary>Comment les mots de passe devraient-ils être stockés ? Pourquoi ?</summary>PBKDF2, hash salé couteux</details>
* <details><summary>Sachant que vous ne disposez pas des mots de passe en clair mais uniquement des hash MD5, proposez une démarche de migration vers votre nouvelle solution.</summary>renouvellement lors de la connexion des usagers</details>


<details>
<summary>Q2 - Proposez un protocole basé sur de la cryptographie asymétrique permettant l'authentification d'un client par un serveur. Vous devez décrire  le matériel cryptographique initialement en possession du client et du serveur ainsi que les messages échangés lors de l'authentification. Un attaquant peut observer ou modifier le canal, ce qui peut faire échouer l'authentification. Si l'authentification réussit, le serveur est certain de communiquer avec le bon client et un canal de communication sûr (chiffré) a été mis en place.</summary>
Le serveur doit authentifier le client : le client a une paire de clés publique/privée, soit le client a un certificat signé par une CA reconnue par le serveur, soit le serveur connaît la clé publique du client. Le serveur doit challenger le client pour vérifier qu'il possède la clé privée associée. Une clé de session peut-être envoyée par le serveur ou un Diffie-Hellman authentifié.
</details>

<details>
<summary>Q3 - Proposez un algorithme d'authentification mutuelle basé sur de la cryptographie asymétrique permettant à un serveur d'authentifier un client et au client d'authentifier le serveur. Vous devez décrire  le matériel cryptographique initialement en possession du client et du serveur ainsi que les messages échangés lors de l'authentification mutuelle.</summary>
L'authentification est mutuelle, le client a une paire de clés asymétriques et le serveur également. Soit il y a une CA, chaque participant reconnaît la CA et a un certificat signé par cette CA, soit chaque participant connaît au départ la clé publique de l'autre. Chacun doit challenger que l'autre possède bien la clé privée associée.
</details>

Niveau 3
========

Q1 - D'après Wikipedia, _le chiffrement de bout en bout (en anglais, End-to-end encryption ou E2EE) est un système de communication où seules les personnes qui communiquent peuvent lire les messages échangés. En principe, il empêche l'écoute électronique, y compris par les fournisseurs de télécommunications, par les fournisseurs d'accès Internet et même par le fournisseur du service de communication. Avec le chiffrement de bout en bout, personne n'est en mesure d'accéder aux clés cryptographiques nécessaires pour déchiffrer la conversation. Les systèmes de chiffrement de bout en bout sont conçus pour résister à toute tentative de surveillance ou de falsification, car aucun tiers ne peut déchiffrer les données communiquées ou stockées. En particulier, les entreprises qui offrent un service de chiffrement de bout en bout sont incapables de remettre une version déchiffrée des messages de leurs clients aux autorités._

Proposez la conception cryptographique d'une telle messagerie chiffrée (inscription des utilisateurs, échange de messages, sauvegarde d'un historique de communication). Le serveur ne doit pas pouvoir espionner ou falsifier les communications, même sous la contrainte. Analysez ensuite votre solution, en particulier son ergonomie, sa facilité d'utilisation, ce qui reste éventuellement espionnable, les risques restants et la gestion du changement de périphérique d'un utilisateur (remplacement du smartphone, typiquement). L'utilisabilité de la solution proposée et la qualité de son analyse critique sont importantes.

Q2 - Une carte à puce (carte bancaire, SIM, etc.) est un mini-ordinateur intégrant des clés cryptographiques et offrant des fonctions permettant d'utiliser ces clés. Un code PIN permet de débloquer l'usage de ces fonctions. Une fois débloquées, ces fonctions permettent de chiffrer, déchiffrer, signer, vérifier. Les clés cryptographiques restent toujours dans la puce, elles ne sont jamais exportées, c'est la puce uniquement qui les exploite et ne renvoie que le résultat des opérations demandées.

* Proposez un système de cartes bancaires (il n'est pas nécessaire que cela corresponde au système réel, vous devez faire une proposition pertinente). Vous décrirez notamment la création initiale de la carte, son matériel cryptographique, qui le connaît, ce qui se passe lors d'un paiement.
* Est-il possible, avec votre solution, de faire un faux-paiement avec une fausse carte ? Autrement dit, une carte créée indépendamment, non liée à une banque et à un compte, peut-elle tromper le terminal de paiement et lui faire croire que le paiement est valide (alors que le commerçant ne pourra pas être payé, la carte n'étant attachée à aucun compte bancaire) ? Si cela est possible, quelle solution pouvez-vous proposer ? Vous étudierez le cas où le terminal de paiement a accès au réseau (il peut typiquement interroger une banque de manière interactive) et le cas où le terminal n'a pas accès au réseau. On se concentrera ici sur les aspects réseaux et cryptographiques, pas sur l'aspect visuel de la carte.

_Les YesCards étaient de fausses cartes qui permettaient ce type d'attaque. La vulnérabilité associée a bien sûr depuis été corrigée._
