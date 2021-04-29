# TD 4 : Autorités de certification

_François Lesueur ([francois.lesueur@insa-lyon.fr](mailto:francois.lesueur@insa-lyon.fr))_

Ce TD présente le modèle de PKI "Autorités de certification", généralement noté CA (_Certification Authority_). Pour rappel, dans le cas du HTTPS par exemple, une CA doit permettre de valider la clé publique tierce obtenue pour la connexion au site demandé.

Dans le mode distanciel, réfléchissez en groupes de 4 dans des salons de discussion spécifiques. Des éléments de réponse sont accessibles pour chaque question (en cliquant sur les questions) : réfléchissez sans ces éléments, puis regardez et intégrez ces éléments. L'enseignant fera le tour des groupes pour échanger sur les points nécessaires.

Notations
=========

* h(m) est le hash du message m
<!-- * Si K<sub>A</sub> est une clé symétrique, {m}<sub>K<sub>A</sub></sub> est le chiffré de m avec la clé K<sub>A</sub>, m = { {m}<sub>K<sub>A</sub></sub>}<sub>K<sub>A</sub></sub> -->
* Si Pub<sub>A</sub> et Priv<sub>A</sub> sont des clés asymétriques complémentaires publique/privée, {m}<sub>Pub<sub>A</sub></sub> est le chiffré de m avec la clé Pub<sub>A</sub> et m = { {m}<sub>Pub<sub>A</sub></sub>}<sub>Priv<sub>A</sub></sub>
* m signé avec la clé Priv<sub>A</sub> est noté m.{h(m)}<sub>Priv<sub>A</sub></sub>


Point de départ et objectif
===========================

Nos deux interlocuteurs sont Alice (client HTTPS, ie, un navigateur web) et Bob (serveur HTTPS, ie, un serveur web). Même si le protocole permet l'authentification mutuelle (chaque acteur authentifie cryptographiquement l'autre), nous allons étudier le cas le plus diffusé où seul le client HTTPS authentifie le serveur HTTPS. L'authentification permet d'établir un canal sécurisé en sachant que la bonne personne est de l'autre côté : il faut pour cela connaître la bonne clé publique de son interlocuteur.

Nous allons décrire au fur et à mesure la connaissance des différents acteurs. Au départ, Alice n'a pas de connaissance particulière, Bob connaît son couple de clés Pub<sub>B</sub>/Priv<sub>B</sub> (c'est lui qui l'a généré).

L'objectif est qu'Alice obtienne la connaissance (B, Pub<sub>B</sub>), ie, l'association valide de la clé publique de Bob à son identité.



Échange direct
==============

Alice et Bob communiquent à travers un canal non sécurisé. La première façon pour Alice d'obtenir l'association attendue serait de la demander à Bob à travers ce canal. C'est ce qu'il se passe lorsque l'on parle, en HTTPS, de _certificats auto-signés_.

1. <details><summary>Sans prendre en compte la sécurité, est-ce que cela peut fonctionner ?</summary>Oui, on obtient en général une clé fonctionnelle</details>
2. <details><summary>Si cela fonctionne, quel peut être le risque (en prenant maintenant en compte la sécurité) ? A-t-on gagné quelque chose par rapport à une communication en clair ?</summary>S'il y a un attaquant, il peut remplacer la clé sur le chemin. On a en fait rien gagné : soit il n'y a pas d'attaquant sur le chemin, on obtient la bonne clé mais la crypto ne sert pas à grand chose (vu qu'il n'y a pas d'attaquant) ; soit il y a un attaquant et on se fait MitM</details>
3. <details><summary>Décrivez une attaque possible par <a href="https://fr.wikipedia.org/wiki/Attaque_de_l%27homme_du_milieu">man-in-the-middle</a>.</summary>L'idée est de modifier la clé en chemin et de s'interfacer dans la communication, il faut détailler.</details>

Une PKI, et donc par exemple une CA, vise à sécuriser l'obtention de cette association (identité, clé publique).

> Un premier type d'alerte de sécurité des navigateurs concerne ces certificats auto-signés.

Ajout d'un nouvel acteur : la CA
========================

Nous intégrons un troisième acteur C (CA), qui va agir comme un tiers de confiance, et ajoutons les connaissances suivantes :

* C connaît Pub<sub>C</sub>/Priv<sub>C</sub> (son couple de clés)
* A connaît Pub<sub>C</sub> et fait confiance à C
* L'objectif est que C certifie beaucoup d'associations (identité, clé publique), afin de servir de pivot unique pour de nombreuses communications

1. <details><summary>À partir du cours, refaites la cinématique de CA/HTTPS dans ce modèle : les échanges entre B et C, puis entre B et A (A et C ne communiquent jamais directement !). Quel élément est le certificat ? Vous utiliserez les notations présentées en début de sujet.</summary>B fait une demande de certificat, il envoie pour cela (B, Pub<sub>B</sub>) à C. C lui envoie en réponse le certificat (B, Pub<sub>B</sub>).{h((B, Pub<sub>B</sub>))}<sub>Priv<sub>C</sub></sub>, qui est l'association signée par sa clé privée. Enfin, B envoie à A ce certificat (B, Pub<sub>B</sub>).{h((B, Pub<sub>B</sub>))}<sub>Priv<sub>C</sub></sub></details>
2. <details><summary>Comment C vérifie-t-elle l'association déclarée (B, Pub<sub>B</sub>) ?</summary>Il n'y a pas de cryptographie possible à ce niveau, C ne connaît pas B initialement. Ce sont d'autres moyens : réception d'un mail (est-ce sécurisé ?), coup de téléphone, envoi d'un paquet par internet (mais sans authentifier B, donc). Pas de preuve de validité cryptographique ici, et c'est donc largement perfectible : pas de miracle !</details>
3. <details><summary>Comment A vérifie-t-elle l'association obtenue (B, Pub<sub>B</sub>) ? Quelle est la chaîne de confiance ?</summary>En vérifiant la signature grâce à Pub<sub>C</sub>. A fait confiance à C, qui a confiance en l'identité de B.</details>
4. <details><summary>Que déduire si le certificat reçu par A est bien signé mais pour une identité différente de B ? (en HTTPS, l'identité attendue, B par exemple, correspond au nom d'hôte de la requête, par exemple `www.insa-lyon.fr` pour une requête à `https://www.insa-lyon.fr/index.html`)</summary>On en déduit que la réponse ne vient (peut-être) pas du serveur attendu (n'importe qui peut avoir un certificat bien signé pour un autre nom), donc on est pas dans les conditions de sécurité. Le navigateur vérifie que le certificat est valide ET correspond bien à l'identité demandée.</details>

> Un second type d'alerte de sécurité des navigateurs concerne des certificats bien signés mais valides pour un autre site.

> Un certificat est essentiellement cette association (identité, clé publique) assortie d'une durée de vie limitée, le tout signé par une autorité de certification. La norme X509v3 contient évidemment de nombreux autres champs.

<!--
3. Comment A peut-il obtenir Pub<sub>C</sub> pour faire confiance à C ? Quelle sécurité ?
4. Comment C peut-il vérifier l'association (B, Pub<sub>B</sub>) ? Quelle sécurité ?
-->



L'écosystème HTTPS
==================

Ce modèle est tout à fait possible avec une unique CA. Cependant, en pratique, il s'est développé avec une multitude de CA, notamment pour HTTPS. Chaque serveur a le choix de quelle CA il veut être certifié. Du coup, un navigateur reconnaît typiquement de l'ordre d'une petite centaine de CA différentes.

Imaginez maintenant que l'une des autorités soit compromise (malveillante ou attaquée):

1. <details><summary>Quel impact pour les clients reconnaissant cette autorité ?</summary>Ils accepteront potentiellement de mauvais certificats (puisqu'ils auront une signature valide pour le site demandé)</details>
2. <details><summary>Quel impact pour un site dont le certificat est émis par une autre autorité ?</summary>Il a perdu aussi, puisque ses usagers, qui reconnaissent cette CA compromise, accepteront potentiellement une autre clé lorsqu'ils tenteront de s'y connecter, il n'a pas la main sur ce que croiront ses usagers</details>

<!-- DNS CAA https://fr.wikipedia.org/wiki/DNS_Certification_Authority_Authorization -->



Révocation
==========

La certification est un processus _hors-ligne_, c'est-à-dire qu'une fois émis, un certificat reste valide jusqu'à une date fixée lors de la signature (typiquement en années). Il ne s'agit pas d'une validation interactive valable à l'instant de la requête HTTPS.

Dans ses processus, une CA doit donc permettre de révoquer des certificats lorsqu'un site se fait voler sa clé privée.

CRL
---

La CRL (_Certificate Revocation List_) est une liste des certificats révoqués, émise et tenue à jour par la CA.

1. <details><summary>En quoi l'utilisation de CRL va à l'encontre de l'approche hors-ligne (non interactive) et quel risque cela pose pour la CA ?</summary>Le principe de CRL suppose que les navigateurs doivent régulièrement pouvoir interroger la CA, ce qu'ils ne faisaient pas avant (seuls les serveurs le faisaient). Le risque est ainsi pour la CA de devoir gérer d'importants volumes de trafic, liés au nombre d'usagers d'internet et non du nombre de certificats (et donc de clients commerciaux) qu'elle émet.</details>
2. <details><summary>Que faire en cas de CRL non à jour et de CA non disponible pour mettre à jour ?</summary>Bonne question, hein ? On bloque ? On laisse passer dans le doute ? Si on bloque, on a des risques de DoS. Si on laisse passer, un DoS sur la CA permet de duper un usager... Concrètement, pas de très bonne solution, et les CRL pour toutes ces difficultés n'ont jamais été diffusées par les CA pour les certificats classiques (ni, du coup, implémentés dans les navigateurs)</details>


OCSP
----

OCSP (_Online Certificate Status Protocol_) permet à un client de vérifier en temps réel la validité d'un certificat auprès de la CA émettrice.

1. <details><summary>Cela résoud-il le risque que l'utilisation de CRL fait peser sur les CA ?</summary>Pas du tout, puisque maintenant tous les usagers de GMail vont aller toquer chez la CA pour vérifier, cela fait du volume. La CA a un client commercial (GMail) et se retrouve à devoir gérer un flux lié à la popularité de ce client, ce qui décorelle les ressources nécessaires du nombre de ses clients commerciaux</details>
2. <details><summary>Avec l'agrafage OCSP (_stapling_), c'est le serveur web qui demande à la CA une preuve de validité valable 24h et la présente ensuite à ses clients. Cela résoud-il la surcharge de la CA ? Quelle différence par rapport à des certificats valables 24h ?</summary>Oui, cela résoud la surcharge. Cela revient au même que des certificats valables 24h, ne nécessitant donc pas vraiment de révocation. La charge de la CA est cette fois proportionnelle au nombre de ses clients commerciaux.</details>
3. <details><summary>Que faire en cas d'absence d'agrafage OCSP ?</summary>Toujours le même problème. Il faudrait refuser. Mais dans 99% des cas c'est une erreur de gestion. Donc les navigateurs, pour éviter que leurs utilisateurs s'en détournent et en choisissent un autre (guerre de parts de marché), ont tendance à favoriser le fonctionnement et peuvent être laxistes (sur ce point ou d'autre, je n'ai pas vérifié en détail). C'est un vrai point délicat, l'acceptation entraîne évidemment le risque de casser tout l'édifice.</details>

La révocation est un problème qui n'est toujours pas traité de manière satisfaisante et uniforme...


Organisation d'une CA à étages
==============================

Pour limiter les risques et impacts d'une compromission, chaque certificat a une durée de vie limitée, spécifiée dans l'association. Les CA emploient de plus plusieurs clés de niveaux de sensibilité différents. Cela permet d'avoir une ancre de confiance connue par A avec une longue durée de vie (par exemple 30 ans) tout en utilisant quotidiennement du matériel cryptographique avec une durée de vie plus courte (par exemple 1 an).

C a ainsi, à l'instant _t_ :

* Pub<sub>CL</sub>/Priv<sub>CL</sub>, les clés longues, liées au certificat _racine_
* Pub<sub>CC</sub>/Priv<sub>CC</sub>, les clés courtes, liées au certificat _intermédiaire_

Typiquement, un certificat racine avec une durée de vie longue (30 ans par exemple) est intégré aux navigateurs. La clé privée associée à ce certificat est stockée hors-ligne et est utilisée, chaque année, pour signer un certificat intermédiaire avec une durée de vie plus courte (1 an). C'est ensuite ce certificat intermédiaire qui est utilisé au quotidien.

1. <details><summary>Formalisez cette organisation (matériel côté CA, matériel côté site, matériel côté client).</summary>Côté CA : Pub<sub>CL</sub>/Priv<sub>CL</sub>, Pub<sub>CC</sub>/Priv<sub>CC</sub>, Pub<sub>CC</sub>.{h(Pub<sub>CC</sub>)}<sub>Priv<sub>CL</sub></sub><br>Côté site : (B, Pub<sub>B</sub>).{h((B, Pub<sub>B</sub>))}<sub>Priv<sub>CC</sub></sub>.Pub<sub>CC</sub>.{h(Pub<sub>CC</sub>)}<sub>Priv<sub>CL</sub></sub><br>Côté client : Pub<sub>CL</sub></details>
2. <details><summary>Quel est le chemin de vérification pour le client ?</summary>Le serveur envoie (B, Pub<sub>B</sub>).{h((B, Pub<sub>B</sub>))}<sub>Priv<sub>CC</sub></sub>.Pub<sub>CC</sub>.{h(Pub<sub>CC</sub>)}<sub>Priv<sub>CL</sub></sub>, qui contient : l'association (B, Pub<sub>B</sub>), sa signature avec la clé Priv<sub>CC</sub>, la clé publique Pub<sub>CC</sub> et la signature de cette clé publique avec la clé Priv<sub>CL</sub><br>Le client vérifie cette chaîne en partant de Pub<sub>CL</sub>, qui permet de vérifier que Pub<sub>CC</sub> est valide, et ensuite utilise Pub<sub>CC</sub> pour valider (B, Pub<sub>B</sub>)</details>
3. <details><summary>Comment remédier dans le cas où un certificat intermédiaire est compromis ? Dans le cas où le certificat racine est compromis ?</summary>Intermédiaire : on pourrait le révoquer, si la révocation marchait ;).<br>Racine : c'est ancré dans la distribution logicielle du navigateur, il faut que l'éditeur du navigateur propose une mise à jour puis que l'utilisateur applique cette mise à jour (assez efficace sur ordinateur, beaucoup moins sur smartphones avec les anciens qui ne reçoivent plus de mise à jour, pire sur l'équipement spécifique industriel/médical/IoT)</details>
