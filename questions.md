Questionnaire 4TC-CSC
=====================

Les questions sont organisées en 3 niveaux :

* Niveau 1 : C'est une question simple, la réponse est disponible à côté. La préparation du cours doit permettre d'y répondre directement.
* Niveau 2 : C'est une question moyenne, des éléments de réponse seulement sont fournis. La compréhension du cours doit permettre de répondre.
* Niveau 3 : C'est une question compliquée, sans correction unique, à discuter de vive voix.

Les réponses'

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

* des mesures pour s'assurer le contrôle sur l'établissement de normes américaines et internationales de chiffrement (NIST, normes ISO),
* la collaboration avec des entreprises technologiques pour intégrer — dès la conception — des portes dérobées dans leurs solutions de chiffrement (logiciels ou puces électroniques),
* la collaboration avec des fournisseurs de services Internet pour récupérer des certificats de chiffrement,
* l'investissement dans des ordinateurs à hautes performances,
* voire des cyberattaques ou l'espionnage des sociétés pour leur voler leurs clés numériques.
</details>

<details>
<summary>Quel algo a gagné la compétition AES ?</summary>
Rijndael
</details>



PKI
---

<details>
<summary>Qu'est-ce qu'une PKI ?
	* Un système permettant d'associer une clé publique à une identité
	* Un synonyme d'autorité de certification
	* Un synonyme de toile de confiance
	* Un serveur dédié à la récupération de clés privées</summary>

Un système permettant d'associer une clé publique à une identité
</details>

<details>
<summary>Quelle garantie nous offre a priori une PKI ?
	* Que la communication pourra être confidentielle et intègre
	* Que ma machine ne sera pas compromise lors de la communication
	* Que le serveur auquel je vais me connecter est bien celui qu'il prétend être
	* Que le serveur auquel je vais me connecter n'est pas compromis</summary>
1 et 3
</details>

<details>
<summary>En l'absence de PKI, comment établir une communication sécurisée sans connaissance préalablement partagée avec mon interlocuteur ?</summary>
Je ne peux pas
</details>




<details>
<summary>En général, comment sont validées les demandes de certificats par les CA ?
	* Par email
	* Par courrier postal
	* En personne
	* Par un formulaire administratif géré par chaque état
</summary>
Par email
</details>

<details>
<summary>Le marché des CA est opéré par des entreprises privées, des administrations publiques, des ONG et associations ou les auteurs de navigateurs web ?</summary>

Des entreprises privées
</details>

<details>
<summary>Dans la toile de confiance :
	* Il y a un point central
	* Chaque participant a un rôle équivalent
	* Chacun choisit explicitement à qui il fait confiance
	* Le fonctionnement est simple et automatique
</summary>
2 et 3
</details>

<details>
<summary>Du point de vue de l'utilisateur final côté client web, quelle PKI entre CA et PGP demande le moins d'expertise/de travail ?</summary>
CA
</details>

<details>
<summary>Avec DANE, quel sont les points de confiance les plus importants ?
	* La racine DNS ?
	* Les registrars ?
	* Les autorités de certification ?
	* Les utilisateurs du système ?
</summary>
La racine DNS et les registrars
</details>





