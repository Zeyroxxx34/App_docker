from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import psycopg2

app = FastAPI(title="TD Docker API", version="1.0.0")

#CORS pour le navigateur
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:8080").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,    
    allow_credentials=True,
    allow_methods=["GET"],            
    allow_headers=["Content-Type"],   
)

#Récupération des variables du fichier .env
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

#Route pour vérifier que l'API est opérationnelle
@app.get("/status")
def status():
    return {"status": "OK"}

#Route pour récupérer les données depuis PostgreSQL
@app.get("/items")
def items():
    #Connexion à la BDD
    conn = psycopg2.connect(
        host = DB_HOST, port = DB_PORT,
        user = DB_USER, password = DB_PASSWORD, dbname = DB_NAME
    )
    cur = conn.cursor()
    #Requête pour récupérer les items
    cur.execute("SELECT id, name FROM items;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in rows]