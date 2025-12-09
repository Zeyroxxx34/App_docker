# App_docker

# Conception d'une application conteneurisée générique

## Description

### Application full-stack containerisée utilisant :

Frontend : Code natif (html, JS)

Backend : FastAPI

Base de données : PostgreSQL

Containerisation : Docker

Cette application implémente des données stockées dans PostgreSQL, exposées via FastAPI et visualisable depuis un navigateur web.


## Architecture du projet

```

TD_Docker/
├─ api/                          # Backend FastAPI
│  ├─ Dockerfile  
│  ├─ main.py     
│  └─ requirements.txt          
├─ front/                        # Frontend natif
│  ├─ Dockerfile
│  ├─ index.html
│  ├─ script.js
├─ .env
├─ .gitignore
├─ docker-compose.yml            # Définition des services Docker
├─ env.example
└─ README.md                    
```


## 0. Prérequis

Docker (version récente)


## 1. Build des images Docker

### Cette étape construit toutes les images nécessaires pour le projet :
```
docker compose build
```

### Vérifier que les images ont bien été crées avec : 
```
docker images
```

## 2. Lancer les conteneurs

### Une fois les images construites, démarrer les services avec :
```
docker compose up
```
Cette commande lance PostgreSQL, FastAPI et le frontend natif.
Le frontend sera accessible sur http://localhost:8080
Le backend sera accessible sur : http://localhost:5000/items pour la liste des items
                                 http://localhost:5000/status pour le status de l'API


## 3. Arrêter les conteneurs

### Pour stopper et supprimer les conteneurs tout en conservant les volumes :
```
docker compose down
```
### Pour stopper et supprimer les conteneurs sans conserver les volumes (peut être utile si problèmes de connexion entre l'API et la BDD) :
```
docker compose down -v
```

## 4. Développement

### Lors de modifications du code (Frontend ou Backend), il est nécessaire de reconstruire l’image Docker des services avant de relancer les conteneurs afin que les changements soient pris en compte :
```
docker compose build
docker compose up
```

## 5. Push une image signée sur Docker Hub

### Dans le terminal du projet, activer Docker Content Trust :
```
$env:DOCKER_CONTENT_TRUST=1
```
### Ensuite, il suffit de se loguer à son compte Docker avec la commande (après avoir créé deux repositories dans Docker Hub : dans mon cas, api et front) :
```
docker login
```
### Ensuite, build et tag les images :
```
docker build -t username_dockerHub/api:latest ./api
docker build -t username_dockerHub/front:latest ./front
```
### Enfin, push les images avec cette commande :
```
docker push username_dockerHub/api:latest
docker push username_dockerHub/front:latest
```
Il est possible de vérifier si une image est signée en essayant de la pull avec le Docker Content Trust d'activé, si le pull fonctionne, l'image est signée.

### Dans mon cas, j'arrive à push une image non signée mais lorsque je veux la signer j'ai cette erreur :
```
failed to sign docker.io/username_dockerHub/api:latest: no hashes specified for target ""
```
### Dans Docker Hub, il est possible de retrouver mes deux images :

zeyroxxx/api
zeyroxxx/front


## 6. Scanner une image

### Pour scanner une image, il suffit d'exécuter cette commande :
```
docker scan username_DockerHub/api:latest
docker scan username_DockerHub/front:latest
```
### Dans mon cas (les issues correspondent à des fichiers inconnus non reliés à mon code) :
```
Organization:      zeyroxxx34
Package manager:   deb
Project name:      docker-image|zeyroxxx/api
Docker image:      zeyroxxx/api:latest
Platform:          linux/amd64
Target OS:         Debian GNU/Linux 13 (trixie)
Licenses:          enabled

Tested 87 dependencies for known issues, found 23 issues.
```

## 7. Automatisation

Le fichier deploiement.sh permet de build les images et lancer les conteneurs automatiquement.
