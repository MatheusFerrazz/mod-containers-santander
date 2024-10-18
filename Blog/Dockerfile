# Usa a imagem base do Ubuntu
FROM ubuntu:22.04

# Desativa as interações durante a instalação de pacotes
ENV DEBIAN_FRONTEND=noninteractive

# Define variáveis de ambiente para o MySQL
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=wordpress
ENV MYSQL_USER=wp_user
ENV MYSQL_PASSWORD=wp_password

# Atualiza o sistema e instala dependências
RUN apt update && apt install -y \
    apache2 \
    mysql-server \
    php \
    php-mysql \
    wget \
    unzip \
    && apt clean

# Remove os arquivos padrão do Apache
RUN rm -rf /var/www/html/*

# Baixa o WordPress e move os arquivos para o diretório web
RUN wget https://wordpress.org/latest.zip \
    && unzip latest.zip \
    && mv wordpress/* /var/www/html/

# Ajusta permissões do diretório web
RUN chown -R www-data:www-data /var/www/html/

# Configura o banco de dados para o WordPress
RUN service mysql start && \
    echo "CREATE DATABASE wordpress;" | mysql -u root -p$MYSQL_ROOT_PASSWORD && \
    echo "CREATE USER 'wp_user'@'localhost' IDENTIFIED BY 'wp_password';" | mysql -u root -p$MYSQL_ROOT_PASSWORD && \
    echo "GRANT ALL PRIVILEGES ON wordpress.* TO 'wp_user'@'localhost';" | mysql -u root -p$MYSQL_ROOT_PASSWORD && \
    echo "FLUSH PRIVILEGES;" | mysql -u root -p$MYSQL_ROOT_PASSWORD

# Exponha a porta 80 para o Apache
EXPOSE 80

# Copia o script de inicialização
COPY script.sh /script.sh
RUN chmod +x /script.sh

# Define o comando padrão para iniciar o container
CMD ["/script.sh"]