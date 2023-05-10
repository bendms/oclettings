## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Pipeline CI/CD

Pour mettre en place la pipeline CI/CD, vous utiliserez les outils suivants : 

- Docker
- Sentry
- Heroku
- CircleCI

### Docker

- Rendez-vous sur https://hub.docker.com/signup/ pour créer votre compte Docker
- Cliquez sur "Create repository"
- Choisissez un "Repository Name" et cliquez sur le bouton "Create"
- Dans le fichier config.yml, remplacer le nom du repository "oclettings" par votre "Repository Name" à la ligne 52, 55, 58 et 61
- Vous connaissez maintenant votre identifiant Docker "DOCKERHUB_USERNAME" et le mot de passe associé "DOCKERHUB_PASS"

### Sentry

- Commencez par créer votre compte sur la page https://sentry.io/signup/ 
- Une fois connecté, rendez-vous dans la section "Project" et cliquez sur "Create Project"
- Choisissez Django, indiquez la frequence des alertes que vous souhaitez avoir et choisissez le nom de votre projet
- Une page va s'ouvrir dans laquelle vous aurez accès à votre "SENTRY_DSN"

### Heroku

- Créer votre compte Heroku depuis https://signup.heroku.com/
- La double authentification par défaut sera activée. Il vous faudra vous munir de votre smartphone et télécharger l'application Salesforce Authenticator (ou autre application du même type pour valider la connexion)
- Cliquez en haut à droite sur votre compte pour accéder à la section "Account Settings", Vous aurez accès à votre "HEROKU_API_KEY" via le bouton "Reveal"
- Depuis la page d'accueil de votre compte, cliquez sur le bouton "New", puis sur "Create new app"
- Indiquez votre "HEROKU_APP_NAME" dans la section "app-name", choisissez votre région et cliquez sur le bouton "Create app"

### CircleCI

Pour commencer, veuillez créer un compte sur CircleCI, vous pouvez vous connecter directement avec votre compte Github. Cela aura pour effet de connecter vos dépôts distants à votre compte CircleCI. 
Une fois cette étape réalisée, vous devrez avoir accès à votre projet depuis l'onglet "Projects". 
- Cliquez sur les trois points à droite de votre projet pour accéder à "Project Settings"
- Rendez-vous dans la section "Environmnent Variable" et ajoutez-y les informations suivantes : 
  - DOCKERHUB_PASS
  - DOCKERHUB_USERNAME
  - HEROKU_API_KEY
  - HEROKY_APP_NAME
  - SECRET_KEY
  - SENTRY_DSN

## Déploiement

Pour lancer la pipeline, apporter des modifications à votre code et mettez à jour votre repository Github.

La pipeline est composée de 3 étapes : 

- build-test-linting

Cette première partie va installer toutes les dépendances du projet contenu dans le fichier "requirements.txt", elle va ensuite exécuter les tests avec Pytest et formater le code afin qu'il respecte les bonnes pratiques de la PEP8 grâce à l'outil Black

Si cette première étapes ne soulève pas d'erreur, la seconde partie va s'exécuter

- build-and-push-to-dockerhub

Cette seconde partie va construire l'image docker de notre projet compilé, se connecter à votre compte Docker, tagger l'image du projet en utilisant le hash du commit que vous aurez réalisé. La pipeline va ensuite envoyer votre image sur Docker Hub

Cette section ne s'exécutera que si les modifications apportées se trouvent sur la branche "main"

- deployment

La dernière partie va installer Heroku CLI, se connecter à votre compte Heroku, configurer la "SECRET_KEY" de Django et le "SENTRY_DSN" de Sentry en tant que variables d'environnement. Il va ensuite utiliser l'image docker précédemment créée et l'envoyer sur votre application Heroku pour enfin la mettre en ligne

Cette section, comme la précédente ne s'exécutera que si les modifications apportées se trouvent sur la branche "main", que les "jobs" build-test-linting et build-and-push-to-dockerhub se soient bien exécutés.