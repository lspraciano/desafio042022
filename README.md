# Projeto de Registro e Avaliação de Transações Bancárias
Esta aplicação tem como principal objetivo analisar transações suspeitas e listar
as transações suspeitas. Este foi um projeto sugerido em um desafio da plataforma
de ensino ALURA, mas estou incrementado algumas funcionalidades não listadas
para este desafio, como exemplo a Tabela SQL de auditória de modificações
nos usuários e uma HomePage com Dashboards.

## Status do Projeto
 - Em Desenvolvimento
 - 90% Completo
 - Previsão de Término: 15/06/2022

## Tecnologia Usada
### Back-End
 1. FLASK
### Front-End
 1. JavaScript
 2. CSS
 3. HTML
### DataBase
 1. Postgresql
### Infraestrutura
 1. Docker
 2. Heroku

## Funcionalidades
1. Login
2. Importar Transações Bancárias através de um arquivo CSV
3. Histórico de Importações
4. Relatório Geral das Transações
5. Relatório de Suspeitas de Fraude
6. Cadastrar, Consultar, Alterar e Deletar usuário do sistema


## Como Ultilizar?
Podemos usar esta aplicação de 3 formas:
1. Acesso via página Web
2. Clonando o Repositório
3. Consumo da nossa API

### 1. Acessando Atráves da página Web:
Nossa app esta disponibilizado para uso atráves do link: 
    
    http://transactions-analyzer.herokuapp.com/

#### 1. Login
Ao acessar o link, você irá se deparar com a nossa tela de login.

![](readme/images/login.png)

Para realizar o acesso criamos as credenciais de acesso para você testar:

    Nome do Usuário: ADMIN
    Senha: 123999


Após realizar o login, o usuário é redirecionado para nossa home page

![img.png](readme/images/home-page.png)

Esta tela é composta por uma barra de menu lateral, dashboards e um menu superior.

Menu Lateral:

    Atrávez do menu de acesso lateral você pode navegar por nossa aplicação e acessar todas
    nossas funcionalidades.

Dashboard:

    Os dados contidos na Dashboard são relativos as transações importadas no mês vigente. 

Menu Superior:

    Essa região contém, a esquerda, o icone para recolher ou mostrar o menu lateral,
    na região central fica o nome da tela, neste caso "Dashboard", a direita encontramos
    o botão para relizar o logout da aplicação.