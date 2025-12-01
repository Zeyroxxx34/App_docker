#Nginx pour servir le site statique
FROM nginx:alpine

#Code du front dans le dossier de Nginx
COPY . /usr/share/nginx/html

#Port exposé pour la page web
EXPOSE 80

#Utilisateur non root déjà existant par défaut dans l'image Nginx Alpine
USER nginx

# Lancer Nginx
CMD ["nginx", "-g", "daemon off;"]
