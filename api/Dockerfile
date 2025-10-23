#Image Python
FROM python:3.12-slim

WORKDIR /app

#Dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Code de l'API
COPY main.py .

#Port exposé pour l'API
EXPOSE 5000

# Exécution de l'API avec uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
