#!/bin/bash
#Autor: Daniel Baco
#Version: 0.1

#Recargar contenedores Docker
#----------------------------

#Tumbar contenedores
docker compose down


#Levantar contenedores
docker compose up -d --build
