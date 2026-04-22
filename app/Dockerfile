FROM nginx:stable

# Borramos lo que trae nginx por defecto
RUN rm -rf /usr/share/nginx/html/*

# Copiamos todo el contenido de tu carpeta local al contenedor
COPY ./html /usr/share/nginx/html/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
