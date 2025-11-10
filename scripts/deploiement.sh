#Variables avec valeurs par défaut
REG=${REGISTRY:-}
ORG=${ORG:-}
REPO=${REPO:-App_docker}
TAG=${TAG:-latest}

#Noms des images Docker
API_IMG="${REG:+$REG/}${ORG:+$ORG/}$REPO:api-$TAG"
FRONT_IMG="${REG:+$REG/}${ORG:+$ORG/}$REPO:front-$TAG"

#Construction des images à partir des Dockerfiles
docker build -t "$API_IMG" -f api/Dockerfile ./api
docker build -t "$FRONT_IMG" -f front/Dockerfile ./front

docker compose up -d
