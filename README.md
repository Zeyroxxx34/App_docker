```
# App_docker
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




2. Lancer les conteneurs




3. Arrêter les conteneurs




4. Développement


```
