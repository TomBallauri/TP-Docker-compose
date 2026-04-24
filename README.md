# MySQL & MongoDB Docker Stack

Stack Docker avec MySQL, MongoDB, leurs interfaces admin (Adminer, Mongo Express) et une API FastAPI.

## Configuration

Copier le fichier d'exemple et renseigner les variables :

cp .env.example .env

| Variable              | Description                           |
|-----------------------|---------------------------------------|
| `MYSQL_ROOT_PASSWORD` | Mot de passe root MySQL               |
| `MYSQL_DATABASE`      | Nom de la base (`ynov_ci` par défaut) |
| `MYSQL_USER`          | Utilisateur MySQL                     |
| `MYSQL_PASSWORD`      | Mot de passe utilisateur MySQL        |
| `MYSQL_HOST`          | Hôte MySQL (ne pas modifier)          |
| `MONGO_URL`           | URL MongoDB (ne pas modifier)         |

## Lancement

docker compose up -d

## Services

| Service       | URL                       |
|---------------|---------------------------|
| API           | <http://localhost:8000>   |
| Adminer       | <http://localhost:8080>   |
| Mongo Express | <http://localhost:8081>   |
