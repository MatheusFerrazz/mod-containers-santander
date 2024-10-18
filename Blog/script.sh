#!/bin/bash

# Inicia o MySQL e o Apache
service mysql start
service apache2 start

# Mantém o container ativo
tail -f /dev/null