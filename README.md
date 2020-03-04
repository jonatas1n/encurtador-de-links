## Visão Geral

## Guia de instalação

Essa aplicação tem seu ambiente configurado através de conteiners Docker, portanto, tem como pré-requisitos a instalação do Docker e Docker-compose.

Também é necessário ter o Git instalado para clonar o repositório.

### Clonar o repositório:

```
git clone https://gitlab.com/pencillabs/encurtador-de-url.git
```

### Execução do conteiner:

```
docker-compose up --build
```

Após esses passos a aplicação deverá estar acessível em:

```
localhost:8000
0.0.0.0:8000
```

O projeto está utilizando sqlite3 como banco de dados.
Para acessar a área administrativa ```(http://localhost:8000/admin)```, use as informações:

```
Username: admin
Password: password
```