FROM ubuntu:22.04

RUN apt update && apt upgrade -y && apt install nginx -y

EXPOSE 80 

CMD ["nginx", "-g", "daemon off;"]