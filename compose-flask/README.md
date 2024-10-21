### Execução:

1. **Construir e iniciar os contêineres**:
No diretório raiz (`/my-microservices-project`), rode o comando:

```
docker-compose up --build
```

2. **Acessar o serviço**:
    - O app principal estará disponível em `http://localhost:5000`.
    - Para fazer uma requisição ao app com validação de token, você pode usar `curl` ou outra ferramenta, por exemplo:

```
curl -H "Authorization: valid-token" http://localhost:5001/validate
```
