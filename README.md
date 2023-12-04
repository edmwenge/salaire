# salaire
salaire est un programme qui demande à l’utilisateur de saisir les noms des employés et leurs salaires pour une entreprise donnée et les stocks dans un tableau

voici une description étape par étape des commandes que j'ai utilisées pour mettre sur git mes travaux:

1. J'ai exécuté la commande git init pour initialiser un nouveau dépôt Git dans le répertoire local de chaque travail.

2. Ensuite, j'ai ajouté tous les fichiers modifiés et nouveaux du répertoire de travail à la zone de préparation (staging area) pour être validés avec la commande git add ..

3. Après avoir ajouté les fichiers, j'ai validé les modifications en utilisant la commande git commit -m"commentaire pour chaque projet" pour créer un nouveau commit avec le message "commentaire".

4. J'ai ajouté un dépôt distant nommé "origin" avec l'URL spécifiée comme point de connexion vers le dépôt distant sur GitHub en utilisant la commande git remote add origin https://github.com/edmwenge/salaire.git (par exemmple).

5. Ensuite, j'ai essayé de pousser la branche principale (main) vers le dépôt distant en utilisant la commande git push -u origin main. Cependant, l'opération a provoqué un rejet car le dépôt distant contenait des travaux que je n'avais pas localement.

6. J'ai ensuite essayé d'exécuter plusieurs commandes pour résoudre le problème de rejet, y compris git merge et git pull. Finalement, j'ai utilisé git merge origin/main --allow-unrelated-histories pour aboutir à une fusion en permettant l'intégration d'historiques non liés.

7. Enfin, après cette opération de fusion, j'ai réussi à pousser mes modifications vers le dépôt distant en utilisant la commande git push origin main.
