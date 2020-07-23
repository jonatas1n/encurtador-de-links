# Teste técnico

## Escopo
Encurtamento de URL é uma técnica utilizada na internet para transformar um endereço HTTP em um link mais curto. Você foi foi designado para desenvolver uma nova plataforma que seja capaz de encurtar urls e mostrar os links mais acessados após o encurtamento.

Você recebeu três histórias de usuário para serem desenvolvidas na primeira sprint do projeto:

1.  Como usuário, gostaria de me autenticar no sistema para ter acesso ao meu perfil;

	-   O usuário deverá se cadastrar na plataforma, informando nome, email e senha;
	-   O usuário deverá se autenticar na plataforma, informando email e senha;
	-   O usuário deverá ser avisado caso o email informado no cadastro já esteja em uso;
	-   Senhas deverão ser salvas utilizando alguma biblioteca de cifragem (criptografia);

2.  Como usuário, desejo encurtar urls para tornar os links da minha plataforma mais agradáveis ao serem compartilhados para outros usuários;

	-   O input deve validar se o texto inserido tem o formato de uma url;
	-   Urls inválidas não poderão ser encurtadas;
	-   Urls encurtadas devem ser únicas;
	-  Uma url que já foi encurtada não deve ser encurtada novamente;

3.  Como usuário, desejo visualizar as urls mais acessadas após o encurtamento;

	-   O ranking deve mostrar apenas as 5 urls mais acessadas;
	-   O ranking deve mostrar a url original, a url encurtada e a totalidade de acessos à url encurtada;

Dada às histórias anteriores, a plataforma deverá ter quatro telas:

	- Tela de login;
	- Tela de cadastro;
	- Ranking com lista de urls encurtadas pelo usuário logado;
	- Tela para realizar o encurtamento;


As seguintes tecnologias poderão ser utilizadas para o desenvolvimento da solução:

	- Frontend: qualquer biblioteca/framework
	- Backend: ruby(Rails), python, NodeJS ou PHP

## Deploy

O deploy de produção deverá ser feito em uma instância do [Heroku](https://www.heroku.com/). O deploy local deverá ser feito
utilizando um arquivo `docker-compose`. Caso o deploy local não funcione, o candidato está automaticamente **desclassificado**.
Caso o deploy no Heroku não funcione, o candidato sofrerá perdas na avaliação.

## Critérios de avaliação

- Organização do código;
- Legibilidade;
- Configuração separada da implementação (https://12factor.net/);
- Testes automatizados (**Aplicação sem testes será desclassificada**);
- Documentação da arquitetura escolhida para a solução;


Como líder do time, você tem liberdade para implementar a solução na arquitetura que preferir. O fluxo de envio da solução deverá
ser da seguinte forma:

	- Faça um fork do repositório [https://gitlab.com/pencillabs/encurtador-de-url];
	- Desenvolva a solução no seu Fork;
	- Abra um Merge Request para o repositório original;

Na descrição do MR, descreva brevemente a solução e inclua o link para a instância no Heroku. O prazo para entrega do projeto é
de uma semana a partir do dia 27/07.
