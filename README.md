```
App_docker

Conception d'une application conteneurisée générique

-- Description --

Application full-stack containerisée utilisant :

Frontend : Code natif (html, JS)

Backend : FastAPI

Base de données : PostgreSQL

Containerisation : Docker

Cette application implémente des données stockées dans PostgreSQL, exposées via FastAPI et visualisable depuis l’interface web.


-- Architecture du projet --


TD_Docker/
├─ api/                          # Backend FastAPI
│  ├─ Dockerfile  
│  ├─ main.py     
│  └─ requirements.txt          
├─ front/                        # Frontend Vite + React
│  ├─ Dockerfile
│  ├─ index.html
│  ├─ script.js
├─ .env
├─ .gitignore
├─ docker-compose.yml            # Définition des services Docker
├─ env.example
└─ README.md                    


-- Prérequis --

Docker (version récente)


-- Installation et exécution --


1. Build des images Docker

Cette étape construit toutes les images nécessaires pour le projet :

docker compose build


2. Lancer les conteneurs

Une fois les images construites, démarrer les services avec :

docker compose up

Cette commande lance PostgreSQL, FastAPI et le frontend natif.
Le frontend sera accessible sur http://localhost:8080
Le backend sera accessible sur http://localhost:5000/items pour la liste des items
Le backend sera accessible sur http://localhost:5000/status pour le status de l'API


3. Arrêter les conteneurs

Pour stopper et supprimer les conteneurs tout en conservant les volumes :

docker compose down

Pour stopper et supprimer les conteneurs sans conserver les volumes (peut être utile si problèmes de connexion entre l'API et la BDD) :

docker compose down -v


4. Développement

Lors de modifications du code (Frontend ou Backend), il est nécessaire de reconstruire l’image Docker des services avant de relancer les conteneurs afin que les changements soient pris en compte.

docker compose build
docker compose up
```
