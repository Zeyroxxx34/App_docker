#Nginx pour servir le site statique
FROM nginx:alpine

#Code du front dans le dossier de Nginx
COPY . /usr/share/nginx/html

#Port exposé pour la page web
EXPOSE 80

# Lancer Nginx
CMD ["nginx", "-g", "daemon off;"]
