# projet-docker
Projet Docker Linux:

-  1 ou plusieurs conteneurs
-  Au moins 1 Dockerfile supérieur à 2 lignes (assez complexe)
-  Docker Compose
-  Un README avec :
    -  Quelques chose de plug and play
    -  Les commandes pour que le conteneur marche
    -  Les scripts à exécuter
    -  Dire ce qui doit être observé 
- Exemple: 
Communication entre plusieurs containers
Application et lien entre conteneur

# Utilisation du projet

Créer si le fichier .env n'existe pas le créer avec le contenu suivant
```
SECRET_KEY=django-secret(edgdfhgkfdhjgdffd54gfdsg456)
DATABASE_HOST=db
DATABASE_PORT=3306
DATABASE_NAME=docker
DATABASE_USER=docker
USER_PASS=docker
ROOT_USER=root
ROOT_PASS=root
```

Lancer les commandes suivantes
```
git clone https://github.com/enzo9741/projet-docker
cd projet-docker
docker-compose build
docker-compose up -d
```

Une fois les containers démarrer deux sites seront disponible:

http://127.0.0.1:8001/ Permettant d'accéder a phpmyadmin
Si l'access est refuser il suffit d'attendre un peu que le serveur mysql finisse de démarrer.

http://127.0.0.1:8000/ Permettant d'accéder au site d'inventaire(Projet utiliser pour l'exemple)
Un sleep de 30s est présent dans le web-entrypoint.sh car malgré le "depends_on: - db" le serveur web démarre avant la base de données se qui fait que le serveur web n'arrive pas
a démarrer correctement sans se sleep.

Les identifiant mysql sont:
User: docker
Password: docker

User root: root
Password: root

Pour utiliser l'application il est nécéssaire de créer en compte pour cela il faut executer les commandes suivante et en suivant les instruction:
```
docker compose exec web python manage.py createsuperuser
```

En cas d'erreur sur le site executer la commande suivante
```
docker compose exec web python manage.py migrate
```