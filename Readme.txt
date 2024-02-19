
Projet: Colt express

Les parties du sujet traitées.

   Afficher nb_wagons wagon avec la locomotive à droite.
   Afficher nb_joueur bandits au-dessus de chaque wagon.
   Afficher Marshall dans la locomotive.
   Afficher des butins (bource(100 ou 200)/bijou(500) il y en a un nombre aléatoire entre nb_wagons et 2xnb_wagons.
   Afficher le butin magot dans la locomotive.
   Afficher les boutons de déplacement lorsque c’est au joueur de planifier les actions à effectuer.
   Afficher un compte rendu à droite de l'écran.
   Vérifier après chaque déplacement de joueur si le joueur est sur un butin si oui il le récupère.
   Vérifier après les déplacement de joueur et de marshall si on est sur marshall si oui on lâche un butin aléatoirement et le joueur monte sur le toit.
   A la fin de tous les tours vérifier qui a le plus d’argent et dit qu’il a gagné.
   
  Pour les déplacements du bandit dans chaque wagon il y a 3 emplacements dedans et 3 emplacements au-dessus et seulement 1 dans la locomotive et 1 au-dessus. Les bandits ne peuvent pas sortir en dehors de ces emplacements.
  Pour les mouvements du Marshall il a 5 chances sur 11 d’aller à droite, 5 chances sur 11 d’aller à gauche et 1 chance sur 11 de ne pas bouger et comme pour les bandits il ne peut pas sortir.

Les problèmes rencontrés et que vous avez réussi à éliminer. 

   Pour utiliser une image python ne trouvant pas l’image j'ai été obligé de mettre le chemin absolu (exemple ligne 7 et 8).
   Les boutons pour les déplacements je n’ai pas réussi à réutiliser les mêmes boutons pour chaque bandit. J’ai été obligé de faire plein de fonctions qui ne marchent que pour 1 bandit.

Les problèmes qui sont présents et que vous n’avez pas pu éliminer

   On ne peut jouer à 1/2/3 joueurs sans problème mais pas à 4.
   Pendant la phase d’action l'affichage ne s’actualise pas après chaque action mais que la fin de toutes les actions de tous les joueurs.
   D'un ordinateur a l'autre le compte rendu peut ne pas avoir la même dimension donc peut couper la fin.

   
