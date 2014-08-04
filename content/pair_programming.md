Title: Introduction au pair programming
Category: Articles
Date: 2014-08-02
Modified: 2014-08-03

L'activité de pair de programming ou la programmation en binôme consiste à
travailler installé côte à côte sur le même poste de travail afin d'achever
une tâche. Le développeur utilisant le clavier est dénomé pilote (driver), le
second est dénomé copilote (navigator). Les deux développeurs collaborant
continuellement en écrivant les tests, le code de production, en échangeant
sur le design... Le rôle du pilote est d'écrire le code alors que le rôle du
copilote (navigator) a pour fonction de prendre plus ou moins de recule. Le
copilote peut par exemple détecté les erreurs de syntaxe, se demander si le
code produit correspond à la qualité attendu (respectons nous les quatre
règles de simplicté ?), détecter les bugs...

La programmation en binôme est le moyen le plus efficace pour créer une **boucle
de feedback portant sur la production de code**. C'est bien plus efficace que la
revue de code.

Les bénéfices constatés sont : 

* meilleure qualité de code,
* plus grande efficacité,
* plus forte motivation,
* permet de développer la transparence et la confiance au sein de l'équipe,
* permet le transfert de connaissances,
* ameliore l'apprentissage.

Beaucoup de manager sont scéptique sur l'aspect efficacité ! Pourtant la
programmation en binôme permet d'atteindre une qualité de code avec gain en
terme de temps qui est de l'ordre de 50%. C'est à dire qu'il faut en environ
deux fois plus de temps à un développeur seul pour arriver à la même qualité
de code. En 1980 Larry Constantine remarque déjà que la production de code
résultant d'un binôme est de bien meilleur qualité car le code produit résulte
de dialogues régulier et est issu de la reflexion de deux cerveaux. Il
conclue par *"Deux programmeurs en tandem ne sont pas redondant, mais constituent
plutôt la route la plus directe pour obtenir une grande efficacité et 
une meilleur qualité."*[^PairIllu] (Constantine 1995). 

Ward Cunningham a exprimé cette idée plus simplement et plus directement de
cette façon : *"If you don't think carefully, you might think that
programming is just typing statements in a programming language."*[^Ward]

Le binômage ne doit pas se limiter à l'écriture du code de production, il doit
également porter sur les activités de design, conception, codage, tests,
déverminage... Plus l'activité est complexe plus le bénéfice du binômage est
important.

Faut-il pour autant imposer cette pratique ? Non, il ne s'agit pas de
l'imposer mais d'inviter et inciter les développeurs à pratiquer ce mode de
travail pour commencer sur une durée d'un mois. Vous verrez alors les "early
adopters" se révéler. Ils feront des émules et améneront l'équipe à adopter
cette pratique et à terme la plupart des développeurs ne souhaitent plus
travailler que de cette façon.

## Six conseils pour bien binômer

* Les deux développeurs participent et contribuent activement à la solution.
Binômer ce n'est pas regarder par dessus l'épaule son binôme. Binômer c'est
deux têtes collaborant pour trouver la meilleure réponse[^AgileFlash].

* Il faut faire tourner les binômes, un binôme qui resterait constitué
plusieurs jours de suite n'est pas sein. Cela peut affecter l'équipe, de plus
vous devez vous assurer que la solution produite a été revue par plus de deux
développeurs même si cela peut induire un surcoût dû au changement de
contexte. La qualité produite doit minimiser ce surcout. Bref changer de
binôme de une à deux fois par jour.

* Binômer doit rester un plaisir pour cela il faut un environnement
confortable et adapté c'est à dire des bureaux permettant d'accueillir deux
développeur travaillant côte à côte (voir [The Art of Agile - partie Sample Workspaces](http://www.jamesshore.com/Agile-Book/sit_together.html)) .

* Tout code de production doit être réalisé en binômant ! Cela ne veut pas
dire que vous avez à binomer tous les jours de la semaine, il y a des tâches
ne produisant pas de code de production.

* Arretez vous de binômer lorsque vous êtes fatigué. Ne pas dépassez de 75% de
son temps de travail en binomage par jour est une limite raisonable.

* Vous souhaitez d'autres conseils à afficher dans votre espace de travail, imprimez 
[le poster de James Shore](http://www.jamesshore.com/Agile-Book/pair_programming.html)

## Six conseils pour détecter un problème de binômage

* Le temps passé aux rôles de pilote et copilote n'est pas équilibré ! Bref un
des deux programmeurs ne souhaite pas lacher le clavier. Comportement que
dénomerons sous le termes de "Nous avons un Pitbull du clavier". Une tiers
personne peut avoir un intervenir notamment si le copilote reste silencieux.

* Vos bureaux ne vous permette pas d'être installé cote à cote, le copilote
doit être en retrait du pilote. Ce n'est pas une situation approprié car les
deux programmeurs doivent pouvoir collaborer aisément, accéder au clavier 
facilement et équitablement. Il ne faut pas favoriser les comportements du
type le pilote programme alors que le copilote reste passivement à observer
le pilote.

* Des débats sans fin se déroulent au sein d'un binôme. Les débats sur
l'analyse d'une solution ne devrait pas prendre plus de 10 minutes. Time boxer
ces débats et éprouver votre idée par une implémentation concrète. Un code
fonctionnant est un argument bien plus tangible qu'un débat stérile à propos
d'un code possible.

* Un binôme dans lequel on constate que l'un travail alors que l'autre se désengage
n'est pas un comportement sein. Changer de partenaire ou prenez une pause, si ce
comportement de désengagement est régulier chez un partenaire, voyez à coacher 
cette personne.

* Un binômage dans lequel il y a une relation malsaine de type : inamicale ou
pire nuisible est un serieux problème. Un des symptomes est une forte
stabilité  dans le binômes, il n'y a pas ou peu de changements dans la
constitution des binomes. En cas de tensions ou de relation nuisible au sein
d'un binôme, il convient d'assenir au plus vite ce type de comportement ou de
considérer une réorganisation de l'équipe.

* L'équipe doit d'avoir un comportement responsable et collaboratif pour
achever le travail. Cependant chacun doit se rendre compte des tâches
personnelles qu'il a mener. Persister à travailler en binômant alors
que des tâches individuelles sont prioritaire ne constitu plus la réponse 
optimale. Il y a un temps pour tout.

Si vous souhaitez obtenir une meilleur qualité de code, des programmeurs
motivés, une plus grande efficacité, un meilleur apprentissage alors essayez
le pratique  de la programmation en binôme tout en gardant à l'esprit ces
douze conseils. Mettre en oeuvre cette pratique est un réel bénéfice pour tout
projet.

[^Ward]: http://en.wikiquote.org/wiki/Talk:Ward_Cunningham
[^PairIllu]: Pair Programming Illuminated - Laurie Williams & Robert Kessler - Addison Wesley 2002 - ISBN: 0-201-74576-3 
[^AgileFlash]: Agile in a Flash - Jeff Langr & Tim Ottinger - Pragmatic Programmers 2011 - ISBN: 978-1-93435-671-5
