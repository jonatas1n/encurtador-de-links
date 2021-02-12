![PetitLink Logo](/react_frontend/src/assets/img/SVG/Animacao.svg)
# **PetitLink**
## Como executar
- Faça o download do repositório;
- Acesse por um terminal;
- Com o Docker instalado em sua estação de trabalho, Execute os seguintes comandos:
		
		docker-compose build
		docker-compose up

- Aguarde alguns instantes; e
- Acesse http://localhost:8880;
- Experimente a aplicação;
  
## Como executar os testes automatizados
Os testes automatizados foram executas com foco em dois aspectos:
- Estabilidade das regras de negócio
- Eficiência da interface gráfica.

Para executa-los, basta

___

# Arquitetura

## Introdução
Esta aplicação tem como objetivo encurtar endereços URL longos demais a fim de facilitar seu compartilhamento e memorização, podendo aumentar o engajamento relacionado ao conteúdo do site. 
Neste documento, irei descrever o contexto do desenvolvimento deste site, as ferramentas utilizadas, os parâmetros de análise de requisitos e as funcionalidades aplicadas.

## Visão Geral
<!-- Adicionar uma imagem aqui descrevendo as camadas do site -->

A arquitetura de referência foi o Model-View-Controller, mas algumas adaptações e simplificações foram necessárias devido a simplicidade do projeto em relação às regras de negócio e às rotas. A alteração mais importante foi o desenvolvimento das camadas de visualização e Controle dentro do mesmo container, na mesma framework do frontend, já que não eram necessárias grandes redirecionamentos.

A camada de Modelo é representada por uma API desenvolvida com a framework Flask, na linguagem Python, e o gerenciador do banco de dados também escrito em Python, utilizando o banco serverless SQLite3. 
Essa camada é a segunda mais profunda do sistema, e só é acessada pela camada de controle.

A camada de Controle, simplificada tal qual a descrição do primeiro parágrafo deste tópico, foi descrita no arquivo **App.js**, no diretóro **/react_frontend**. O roteamento das páginas foi feito nesse arquivo, e foi utilizado o NGINX para realizar o Proxy Reverso e fazer os redirecionamentos para a API.

A camada de Visualização foi desenvolvida com a framework React, na linguagem Javascript. Duas telas foram desenvolvidas seguindo os requisitos propostos: Uma tela de início, onde o usuário faz a inserção da URL para ser encurtada e pode ter acesso a opção de personalização deste link. A outra tela é a de exibição da URL encurtada, junto com o ranking dos 5 links encurtados mais acessados da ferramenta.

## Requisitos não-funcionais
### Usabilidade
- Reduzir ao máximo a quantidade de telas e seções do aplicativo para facilitar o destaque das informações importantes no serviço.
### Versatilidade
- O usuário deve ter acesso a opções de personalização de seus links para que eles sejam mais amigáveis e aumentem seu alcance.

## Fundamentação
### Banco de dados
O banco de dados escolhido foi o SQLite. Seu principal destaque foi a simplicidade de implementação: Com pouco código além dos comandos em SQL, foi possível fazer a implementação de todo o banco. Além disso, sua característica serveless permitiu sua implementação sem a necessidade de um conteiner individual, reduzindo o numero de roteamentos.
### API
Utilizou-se a framework Flask para a implementação da API. Pareada ao serviço, essa framework é excelente para projetos de pequeno porte, e com poucas linhas de código estrutura todas as rotas e métodos necessários para as inserções e requisições para o banco de dados
### Docker
Para fazer o melhor versionamento das camadas, utilizou-se a ferramenta Docker para reduzir os problemas com compatibilidade e facilitar a execução e o deploy.
### NGINX
Objetivando integrar os conteiners do serviço, utilizamos uma ferramenta de proxy reverso que a partir de redirecionamento pelos caminhos, foi possível integrar todos conteiners necessários e unificar a porta de acesso da aplicação.
### React
Para implementar uma interface dinâmica e com requisições com complexidade suficiente, foi decidida a utilização da framework React. 