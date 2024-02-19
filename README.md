# Ensemble de Julia

Ce projet vise à créer une implémentation simple mais efficace pour générer et visualiser l'ensemble de Julia en utilisant Python avec la bibliothèque Pillow (Réalisé en 2021)
<br>(https://pillow.readthedocs.io/en/stable/index.html) (https://docs.python.org/3/library/math.html)

## À propos de l'Ensemble de Julia
L'ensemble de Julia est une collection de points dans le plan complexe qui démontre un comportement intéressant sous itération. Il est défini comme suit : soit f_c(z) = z^2 + c une fonction quadratique complexe où c est un nombre complexe constant. L'ensemble de Julia associé à c est l'ensemble des valeurs de z_0 telles que la suite z_{n+1} = f_c(z_n) reste bornée.

## Fonctionnalités
- Génération de l'ensemble de Julia pour une constante complexe c donnée.
- Personnalisation des paramètres tels que la résolution de l'image, couleurs etc...
- Exportation de l'image générée au format PNG.

## Prérequis

### - Python 3
### - `pip install Pillow`

Cela installera la bibliothèque Pillow nécessaire pour exécuter ce projet.



## Exemple d'utilisation
couleur1=(88, 81, 115) 
<br>
couleur2=(163, 157, 203, 1)
<br>
![julia](https://github.com/Isaac955/Julia/assets/123961485/d5ab3f6d-7b05-4bda-89fb-938d5322cc36)
