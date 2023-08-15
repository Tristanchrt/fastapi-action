#!/bin/bash

# Vérification des arguments de ligne de commande
if [ $# -ne 1 ]; then
  echo "Usage: $0 <mongodb_container>"
  exit 1
fi

# Nom du conteneur MongoDB passé en argument de ligne de commande
mongodb_container="$1"

# Date et heure actuelle (sera utilisée pour nommer le dossier de sauvegarde)
backup_date=$(date +"%Y-%m-%d_%H-%M-%S")

# Dossier de sauvegarde (vous pouvez changer ce chemin selon vos préférences)
backup_dir="./backup/${mongodb_container}_${backup_date}"

# Créer le dossier de sauvegarde
mkdir -p "${backup_dir}"

# Effectuer la sauvegarde en utilisant mongodump dans le conteneur Docker
docker exec "${mongodb_container}" mongodump --archive="${backup_dir}/backup_${backup_date}.archive"

# Compression facultative (vous pouvez commenter cette ligne si vous ne voulez pas compresser la sauvegarde)
tar -czvf "${backup_dir}.tar.gz" "${backup_dir}"

# Supprimer le dossier de sauvegarde non compressé (décommentez si vous avez utilisé la compression)
# rm -rf "${backup_dir}"
