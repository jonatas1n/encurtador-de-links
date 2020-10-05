# Teste técnico

## Escopo
Encurtamento de URL é uma técnica utilizada na internet para transformar um endereço HTTP em um link mais curto. Você foi designado para desenvolver uma nova plataforma que seja capaz de encurtar urls e mostrar os links mais acessados após o encurtamento.

Você recebeu três histórias de usuário para serem desenvolvidas na primeira sprint do projeto:

1.  Como usuário, desejo encurtar urls para tornar-las mais simples de serem compartilhadas em outras redes;
	-   O input deve validar se o texto inserido tem o formato de uma url;
	-   Urls inválidas não poderão ser encurtadas;
	-   Urls encurtadas devem ser únicas;
	-  Uma url que já foi encurtada não deve ser encurtada novamente;


2.  Como usuário, gostaria de ao clicar em uma url encurtada, ser redirecionado para a url original;
	-  O usuário deverá ser redirecionado para o encurtador;
	-  O encurtador deverá reconhecer a url encurtada, e redirecionar o usuário para a url original;


3.  Como usuário, desejo visualizar as urls mais acessadas após o encurtamento;
	-   As urls mais acessadas deverão ser apresentadas no formato de ranking;
	-   O ranking deve mostrar apenas as cinco urls mais acessadas;
	-   O ranking deve mostrar a url original, a url encurtada e a totalidade de acessos à url encurtada;


Dada as histórias anteriores, a plataforma deverá ter duas telas:

	- Tela para realizar o encurtamento;
	- Ranking com lista de urls encurtadas;


As seguintes tecnologias poderão ser utilizadas para o desenvolvimento da solução:

	- Frontend: qualquer biblioteca/framework;
	- Backend: ruby, python, NodeJS ou PHP (qualquer biblioteca/framework feitos nessas linguagens);

## Deploy

O deploy local deverá ser feito via `docker-compose`.
Caso o deploy no ambiente local dos avaliadores não funcione, o candidato está automaticamente **desclassificado**.

## Critérios de avaliação

- Organização do código;
- Legibilidade;
- Configuração separada da implementação (https://12factor.net/);
- Testes automatizados (**Aplicação sem testes será desclassificada**);
- Documentação da arquitetura escolhida para a solução;
- Aplicação com código copiado de outros candidatos ou da internet será **desclassificada**.


## Entrega

Como líder do time, você tem liberdade para implementar a solução na arquitetura que preferir. O fluxo de envio da solução deverá
ser da seguinte forma:

- Faça um fork privado desse [repositório](https://gitlab.com/pencillabs/encurtador-de-url);
- Desenvolva a solução no seu fork;
- Ao final do período do teste, envie um email para `contato@pencillabs.com.br`, com o link para o repositório. Vocẽ deverá
utilizar o gitlab, e adicionar os usuários dos avaliadores como contribuidores do seu repositório;

O prazo para entrega do projeto é de uma semana a partir do dia **7/10/2020**.
