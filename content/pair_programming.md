Title: Introduction au pair programming
Category: Articles
Date: 2014-08-02
Modified: 2014-08-03


![Photo pair programming](images/photo_pair_programming.jpg) 
 
L'activité de pair programming ou programmation en binôme consiste à
travailler installé côte à côte sur le même poste de travail afin d'achever
une tâche. Le développeur utilisant le clavier est dénommé pilote (driver), le
second est dénommé copilote (navigator). Les deux développeurs collaborent
continuellement en écrivant les tests, le code de production, en échangeant
sur le design... Le rôle du pilote est d'écrire le code alors que le copilote 
(navigator) a pour fonction de prendre plus ou moins de recul. Le
copilote peut par exemple détecter les erreurs de syntaxe, se demander si le
code produit correspond à la qualité attendue (par exemple: respectons nous les quatre
règles de simplicité ?), détecter les bugs...

La programmation en binôme est le moyen le plus efficace pour créer une **boucle
de feedback portant sur la production de code**. C'est bien plus efficace que la
revue de code.

Les bénéfices constatés sont : 

* meilleure qualité de code,
* plus grande efficacité,
* plus forte motivation,
* permet de développer la transparence et la confiance au sein de l'équipe,
* permet le transfert de connaissances,
* améliore l'apprentissage.

Beaucoup de managers sont sceptiques quant à l'efficacité du pair programming
! Pourtant la programmation en binôme permet d'atteindre une même qualité de
code avec un gain de temps de l'ordre de 50%.  C'est à dire qu'il faut environ
deux fois plus de temps à un développeur seul pour arriver à la même  qualité
de code. En 1980 Larry Constantine remarque déjà que la production de code
résultant d'un binôme est de bien meilleure qualité car le code produit
résulte de dialogues réguliers et est issu de la réflexion de deux cerveaux.
Il conclut par cette phrase : *"Deux programmeurs en tandem ne sont pas
redondant, mais constituent plutôt la route la plus directe pour obtenir une
grande efficacité et  une meilleure qualité."*[^PairIllu] (Constantine 1995).

Ward Cunningham a exprimé cette idée plus simplement et plus directement 
 : *"If you don't think carefully, you might think that
programming is just typing statements in a programming language."*[^Ward]

Le binômage ne doit pas se limiter à l'écriture du code de production, il doit
également porter sur les activités de design, conception, codage, tests,
déverminage... Plus l'activité est complexe, plus le bénéfice du binômage est
important.

Faut-il pour autant imposer cette pratique ? Non, il ne s'agit pas de
l'imposer mais d'inviter et d'inciter les développeurs à pratiquer ce mode de
travail. En réalisant un mois d'essai, par exemple. Cette pratique fera des
émules par l'intermédiaire de leader et progressivement l'équipe à adoptera
ce mode de travail. 

## Six conseils pour bien binômer

* Les deux développeurs participent et contribuent activement à la solution.
Binômer ce n'est pas regarder par dessus l'épaule de son binôme. Binômer c'est
deux têtes collaborant pour trouver la meilleure réponse[^AgileFlash].

* Il faut faire tourner les binômes, un binôme qui resterait constitué
plusieurs jours de suite n'est pas sain. Cela peut affecter l'équipe, de plus
vous devez vous assurer que la solution produite a été revue par plus de deux
développeurs même si cela peut induire un surcoût dû au changement de
contexte. La qualité produite doit minimiser ce surcoût. Bref, mieux vaut
changer de binôme une à deux fois par jour. 

* Binômer doit rester un plaisir. Pour cela, un environnement
confortable et adapté est nécessaire : il s'agit de bureaux permettant d'accueillir deux
développeurs travaillant côte à côte (voir [The Art of Agile - partie Sample Workspaces](http://www.jamesshore.com/Agile-Book/sit_together.html)) .

* Tout code de production doit être réalisé en binômant ! Cela ne veut pas
dire que vous devez binomer tous les jours de la semaine, il existe des tâches
n'ayant pas vocation à développer du code de production.

* Arrêtez vous de binômer lorsque vous êtes fatigué. Ne pas dépassez 75% de
votre temps de travail en binomage, par jour.

* Si vous souhaitez d'autres conseils à afficher dans votre espace de travail, imprimez 
[le poster de James Shore](http://www.jamesshore.com/Agile-Book/pair_programming.html)

## Six conseils pour détecter un problème de binômage

* Le temps passé aux rôles de pilote et copilote n'est pas équilibré ! Bref un
des deux programmeurs ne souhaite pas lâcher le clavier. Comportement que
dénommerons sous les termes : "Nous avons un Pitbull du clavier". Cela peut
nécessiter l’intervention d’une tierce personne, notamment si le copilote
reste silencieux. Ou alors vous pouvez commencer par utiliser un timer afin de changer
de rôle à intervals réguliers.

* Vos bureaux ne vous permettent pas d'être installé côte à côte, donc le copilote
se trouve en retrait du pilote. Ce n'est pas une situation adéquate car les
deux programmeurs doivent pouvoir collaborer aisément, accéder au clavier
facilement et équitablement. Il ne faut pas favoriser les comportements du
type le pilote programme alors que le copilote reste passivement en retrait à
observer le pilote.

* Des débats sans fin se déroulent au sein d'un binôme. Les débats sur
l'analyse d'une solution ne devraient pas durer plus de 10 minutes. "Time boxez"
ces débats et éprouvez votre idée par une implémentation concrète. Un code
fonctionnant est un argument bien plus tangible qu'un débat stérile à propos
d'un code possible.

* Un binôme dans lequel on constate que l'un travail alors que l'autre se
désengage n'est pas un comportement sain. C'est peut être que vous avez besoin
d'une pause ou de changer de partenaire. Si quelqu’un présente un comportement
de désengagement régulier, il peut être utile de coacher cette personne.

* Un binômage dans lequel il y a une relation malsaine de type inamicale ou
pire hostile, est un sérieux problème. Un des symptômes est une stabilité dans
les binômes, avec pas ou peu de changements dans leur constitution. En cas
de tensions ou de relations nuisibles au sein d'un binôme, il convient d'assainir
au plus vite ce type de comportement ou de considérer une réorganisation de
l'équipe.

* L'équipe se doit d'avoir un comportement responsable et collaboratif pour
achever le travail. Cependant, chacun doit se rendre compte des tâches
personnelles qu'il a à mener. Persister à travailler en binômant alors
que des tâches individuelles sont prioritaires ne constitue pas une réponse 
optimale. Il y a un temps pour tout.

Si vous souhaitez obtenir une meilleur qualité de code, des programmeurs
motivés, une plus grande efficacité, un meilleur apprentissage, alors essayez
la programmation en binôme. En gardant à l'esprit ces points permettant
d'éviter quelques écueils. Cette pratique apporte de réels bénéfices, quel que
soit le projet.

[^PairIllu]: Pair Programming Illuminated - Laurie Williams & Robert Kessler - Addison Wesley 2002 - ISBN: 0-201-74576-3 
[^Ward]: http://en.wikiquote.org/wiki/Talk:Ward_Cunningham
[^AgileFlash]: Agile in a Flash - Jeff Langr & Tim Ottinger - Pragmatic Programmers 2011 - ISBN: 978-1-93435-671-5

Photo de [Memlopics sur flickr](https://www.flickr.com/photos/menlopics/)