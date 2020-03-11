# Guia para rodar testes

O Encurtador de Urls usa o docker para criar o ambiente do projeto, dessa forma teremos que rodar os testes dentro do container, e gerar os dados esperados.

Para entrar dentro do container rode:

```
docker-compose exec shortener bash
```

Após entrar no container rode:

```
coverage run manage.py test
```

## Gerando o arquivo Html

Para gerar a tabela html do coverage rode o comando:

```
coverage html
```