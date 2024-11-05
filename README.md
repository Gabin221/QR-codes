# QR-codes
 
Ce script permet de générer un QR code à partir d'un texte et de l'enregistrer en tant qu'image PNG.

## Prérequis

Avant de lancer le script, installez la bibliothèque `segno` :
```bash
pip install segno
```

## Utilisation
Le script inclut une fonction `qrCode` qui prend deux paramètres :

`texte_a_scanner` : le texte ou l'URL que vous souhaitez encoder dans le QR code.
`nom_fichier` : le nom du fichier image PNG où le QR code sera enregistré.
