# Passo 1 - Definir uma Imagem Base
FROM python:3.9-slim 

# Passo 2 - Definir o diretório de trabalho
WORKDIR /app 

# Passo 3 - Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Passo 4 - Instalar as Dependencias do python no conteiner
RUN pip install --no-cache-dir -r requirements.txt

# Passo 5 - Copia o código da aplicação para o WorkDir 
COPY . .

# Passo 6 - Definir uma variável de ambiente
ENV FLASK_APP=app.py

# Passo 7 - Expor a porta 
EXPOSE 5000

# Passo 8 - Definir o comando inicial da aplicação
CMD [ "flask", "run", "--host=0.0.0.0" ]

