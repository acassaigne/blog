# Un pré-requis à l'agilité : un cadre sûr 

## Le cadre de sécurité un levier important au développement de l'agilité
Le cadre de sécurité un levier important à la constitution d'une équipe Agile.


Pour le développement de l'agilité au sein d'une équipe il y a quelques
pre-requis fondamentaux. Le premier est la création d'un "cadre de sécurité" (Make
Safety a Prerequisite) comme le préconise l'approche (Modern
Agile)[http://modernagile.org/]. 

C'est un élément fondamentale qui incombe, en premier lieu, aux managers.

Lorsque ce cadre est posé, cela ouvre la voie à la transparence et à la
confiance qui élargissent le champ des possibles.  

Notre équipe constitué de quatre développeurs et d'un manager est dans cette
situation où un cadre de sécurité a clairement été établi, cela a permis et
permet de développer : la transparence, la confiance, des expérimentations (à
taille limitée, l'agilité nous dit pas de Big Bang), de tirer les enseignement
de ces expérimentations...

Se sont d'excellentes fondations pour le développement de l'agilité, la
sécurité permet de développer la transparence et la confiance. Cela nous
permet d'identifier clairement les problèmes et ainsi d'instaurer un esprit
collaboratif orienté à la résolution de ceux-ci. Nous décidons collectivement
de développer une solution afin de tenter d'apporter une réponse. La solution
développée peut être satisfaisante ou partiellement satisfaisante, il est rare
d'arriver du premier coup à une solution correcte. Oui, nous itérons sur la
résolution de problèmes.

Sans la confiance et la transparence il est bien difficile (impossible ?) 
de construire une équipe Agile. Confiance et transparence sont des valeurs
qui ne se décrête pas mais qui se cultive au sein d'un cadre de sécurité.

Cependant cette nécéssité est souvent mal comprise comme l'énnonce
@MarianneRady via ce tweet :

"The term safe environment is often misunderstood. It's not about being
comfortable. It's about knowing that things will not be held against you. Only
then we can make mistakes, learn and ask questions." Gitte @nativewired at
#accde19

Un cadre de sécurité permet de concevoir, d'expérimenter et d'apprendre ce
qu'il convient de réaliser. Oui, nous avons à traiter des problèmes complexe
où la collaboration et les compétences de tous sont nécessaires. Où nous
pouvons nous exprimer librement pour élaborer les meilleurs solutions, où il
est possible de dire : "Je ne sais pas ou ne ne savons pas, nous devons
explorer, expérimenter... et en tirer les enseignements."

Merci aux managers qui sont conscient de ce point fondamendale et plus encore à
ceux qui apportent leur support pour établir ce cadre de sécurité. 

-- done


# Article 2 : Problem solveur

Nous ne sommes pas juste des développeurs, crafter, codeur, manager,
testeur, coach, UX designer... Nous sommes avant tout des hommes et femmes qui
avons intrinsectment cette capacité à apporter des solutions aux problèmes
auxquels nous sommes confrontés.

Cette merveilleuse faculté est assez universelle, faîtes-en usage au sein de
votre équipe pour développer la collaboration.

C'est ce que nous faisons au sein de notre équipe, nous sommes confrontés à de
multiples problèmes pour lesquels nous devons apporter des réponses. 
Je parle des problèmes courant qu'une équipe de développement à affronter, à titre d'exemples : 
Quel est la meilleur réponse à apporter au métier pour tel ou tel problème, 
Comment devons nous développer cet feature, 
Comment pouvons nous réduire les incidents sur tel chaine de traitements, 
Comment pouvons nous améliorer la CI, 
Comment mettons nous en oeuvre la CD...

Lorsque que nous sommes confronté à un problème, nous l'exposons à l'ensemble 
des membres de l'équipe cela a déjà pour premier objectif de tenter d'établir
une définition claire du problème. La meilleure façon pour l'exposer est de le
décrire sur tableau blanc (de grands tableaux blancs biens utilisés sont la
meilleure façon d'augmenter votre bande passante entre toutes les personnes
concernés).

Une fois le problème clairement défini et exposé nous appliquons cette maxime
de Jerry Weinberg :

 “If you haven’t thought of three possibilities, you haven’t thought enough.”

Il nous faut au moins trois possibles solutions, il n'est pas rare d'en avoir
bien plus même lorsque dans un premier temps les réponses semblent délicate à
faire émerger. 

Nous les considérons toutes mêmes celles pouvant s'avèrer, d'un premier abord,
"stupide" car d'une solution a priori "sutpide" peut émerger une solution simple
et éléguante en y apportant quelques changements. Nous réalisons une première
et rapide évaluation en énumérant les avantages et inconvénients de chacune
des solutions. Souvent, une ou deux solution se dégagent, ils nous faut parfois
expérimenter pour parvenir à dégager une solution.

Je pense qu'il y a également une part de sagesse dans ce cette maxime : 

"Good engineering is less about finding the "perfect" solution and
more about understanding the tradeoffs and being able to explain them.”
— Jaana B. Dogan

Lorsque plusieurs solutions se dégagent, il convient alors d'en retenir une.
Cette prise de décision se fait de manière éclairé et collectivement par dot
voting (c'est problement un point à améliorer, j'y reviendrai dans un prochain
article).

Ca devient alors la solution retenue par l'équipe pour laquelle nous avons
compris les enjeux et pour laquelle nous considérons que c'est le meilleur
compromis (oui aucune solution n'est parfaite). 

Nous sommes alors une équipe aligné vers un objectif clair, compris et accepté
par tous (ce dernier point dépend grandement de votre système de prise de
décision).  

Attention toutefois de ne pas considérer que c'est une réponse définitive. 
Si celle-ci s'avère plus délicate à implémenter que prévue ou si nous découvrons
un inconvénient non négligeable, il se peut que nous ayons à l'adapter ou à
reconsidérer notre choix. Il est assez rare d'avoir de tel déconvenue/mauvaise
surprise, notamment lorsque vous avez à réfléchi plusieurs aux options
possibles tout en considérant avantages et inconvénients... 

Attention la solution mise en oeuvre correspond également à une problématique
dans un context donné.  La solution retenue tiens compte de ce context. Ce
context constituant une partie de l'ennoncé du problème qui se doit être
clairement posé, pour rappel.

Il se peut que cette solution soit à revoir si le contexte évolue, par
exemple si nous avons à  construire une application pour 5 à 20 utilisateurs
simulatnées nous aurons une réponse qui ne sera pas forcément la même si nous
avons à supporter quelques milliers d'utilisateurs simulatnéement.

Dans l'adoption de nos réponse nous préviligions la simplicité en écartant de
fait `l'over-ingennering` et le `platinum-gold quality`. Sans pour autant
renier à la qualité suffissante et indispensable à la maintenance de tout
système qui se veut pérène. 


C'est ce type de reflexion collaborative que nous menons autour des problèmes
que  nous avons à aborder.

Je trouve que les problèmes sont de bons et étranges attracteurs de la
collaboration lorsque ceux-ci sont correctement exposés, ils constituent de
belles invitations à une reflexion collaborative.  

---

 Merci à ceux qui on compris l'importance d'un
tel pre-requis. 

Lorsque ce cadre est présent cela ouvre la voie à l'expérimentation et à
exposer clairement les difficultés. Ce cadre donne de solides fondations à la
collaboration. L'équipe peut alors sans craintes exposer une difficulté ou un
problème et commencer à développer ouvertement une collaboration effective afin de 
s'emparer de des problèmes qui sont de la responsabilité de l'équipe.

Il est alors du devoir de l'équipe de développer une telle attitude. Dans un cadre
sûr la transparence apparait alors comme une valeur naturelle. 

L'équipe doit alors veillé à entretenir et à développer cette valeur. En tant
que membre de l'équipe vous avez ce devoir de transparence tout autant vis à
vis de vos équipiers que de vos managers.



Depuis quelques mois, une équipe poursuit son parcours sur les chemins
escarpés de l'agilité en toute sécurité avec le support de ses managers. 

Nous avons dés le début inssufler un esprit collaboratif au sein de cette
équipe naissante. Le premier élément collaboratif mis en oeuvre fût la
conception émergente réalisée par et pour l'équipe. Ce qu'une approche Scrum
aurait tendance à positionner dans la préparation de sprint. 

Nous réalisons ce type d'atelier lorsque le besoin se fait sentir, en essayant
de respecter le dernier moment responsable (cher au Lean), bien plus efficient
mais plus difficile à maîtriser. L'équipe ayant decidé de travailler avec une
approche Kanban (développement en flux) ce timing des ateliers de conceptions
et de reflexion collaborative apparait naturelle. Nous minimisons l'horizon de
ces ateliers à la user story en développement ou au plus lorsqu'il s'agit d'un
nouveau projet à quelques semaines de développement. Bref pas de Big Up Front
Design, ce que nous constatons c'est que tout plan au delà de trois semaines
est le plus souvent invalidé.  Comprenons nous bien, invalidé par la
découverte de nouveaux éléments, difficultés, possibilités et non pas par un
changement de priorité. 

Oui, nous avons un management grandement Agile car nos priroités sont
clairement établies nous permettant d'être focus, nous terminons ce qui est
commencé.


# mini retro

# dernier moment responsable

# Système de prise de décision

### La force de la collaboration

Il y a toujours plus d'idées dans deux têtes que dans une. Lancez-vous 
dans la co-conception de solutions. Voici comment nous réalisons ces ateliers, 
tout d'abord nous appliquons cette maxime de Jerry Weinberg :

Jerry Weinberg says, “If you haven’t thought of three possibilities, you haven’t thought enough.”



nous tentons de construire une équipe agile 

Vous avez à présenter le problème auquel vous êtes confronté afin d'engager
avec les autres membres de l'équipe une reflexion. Une fois cette reflexion mené

Vous de présenter clairement (de façon pédagogique) 




Lorsque ce cadre existe ou du moins est esquissé, il convient 
alors de le renforcer


"the last responsible moment [:] the moment at which failing to make a decision eliminates an important alternative."
Mary and Tom Popendieck

“delay commitment until the last responsible
moment, that is, the moment at which failing
to make a decision eliminates an important
alternative. If commitments are delayed beyond
the last responsible moment, then decisions are
made by default, which is generally not a good
approach to making decisions.”
— Mary and Tom Poppendieck



Jeremy Miller on delaying decisions until the last responsible moment: “The key is to make decisions as late as you can responsibly wait because that is the point at which you have the most information on which to base the decision.”

And Jeff Atwood:“Deciding too late is dangerous, but deciding too early in the rapidly changing world of software development is arguably even more dangerous. Let the principle of Last Responsible Moment be your guide.”

