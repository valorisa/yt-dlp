# Utilisation de l'image Alpine avec Python
FROM python:3.13-alpine

# Définition du répertoire de travail
WORKDIR /mydir

# Installation de ffmpeg
RUN apk update && apk add --no-cache ffmpeg

# Installation de yt-dlp
RUN pip install --no-cache-dir yt-dlp

# Création d'un utilisateur non-root
RUN adduser -D -S appuser

# Changement vers l'utilisateur non-root
USER appuser

# Définition de l'entrypoint pour yt-dlp
ENTRYPOINT ["/usr/local/bin/yt-dlp"]
