#!/bin/bash
#Autor: Daniel Baco
#Version: 0.1

#Escalar contenedores web y logs Docker a 4 nodos
#------------------------------------------------
docker compose up -d --scale web=4 --scale logs=4
