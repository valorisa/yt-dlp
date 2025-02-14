# yt-dlp
Un outil CLI en Python pour télécharger des vidéos depuis différentes plateformes avec des options de qualité.

## Description
------------

Cet outil permet de télécharger facilement des vidéos depuis différentes plateformes en utilisant `yt-dlp`. Il offre un menu interactif pour choisir la qualité de la vidéo.

## Installation
------------

1. **Python** : Assurez-vous d'avoir Python 3.6 ou supérieur installé.

2. **Clonez le Dépôt** :
```bash
git clone https://github.com/valorisa/yt-dlp.git
cd yt-dlp
```

3. **Créez un Environnement Virtuel** :
```bash
python -m venv venv
source venv/bin/activate
```
4. **Installez les Dépendances** :
```bash
pip install yt-dlp
```

5. **Installez FFMPEG** :
- Sur Alpine Linux : 
```bash
  apk add ffmpeg
```
- Sur d'autres distributions, utilisez votre gestionnaire de paquets habituel.

## Utilisation
------------
Exécutez le script Python :
```bash
python yt-dlp.py
```

Suivez les instructions dans le menu pour entrer l'URL de la vidéo et choisir la qualité souhaitée.

### Exemples

- **Télécharger une Vidéo avec la Meilleure Qualité Disponible** :
```bash
python yt-dlp.py
```
Entrez l'URL de la vidéo
Choisissez l'option "Meilleure qualité disponible"


## Licence
---------

Ce projet est sous licence MIT. Voir le fichier [LICENSE.md](LICENSE.md) pour plus de détails.

## Contribuer
------------

Nous apprécions toute contribution pour améliorer cet outil. Pour contribuer, veuillez cloner le dépôt, apporter vos modifications, et soumettre une pull request.

## Remerciements
--------------

Merci à tous ceux qui ont contribué à `yt-dlp` et aux bibliothèques utilisées dans ce projet.
