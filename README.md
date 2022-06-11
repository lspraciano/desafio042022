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

### O que Falta?
- Recuperação e mudança de senha do usuário
- Documentar como clonar e executar o projeto
- Documentar como consumir nossa API

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

## Como Ultilizar?

Podemos usar esta aplicação de 3 formas:

1. Acesso via página Web
2. Clonando o Repositório
3. Consumo da nossa API

### 1. Acesso via página Web:

#### Funcionalidades do site

1. Autenticação de Usuário
2. Importar Transações Bancárias
3. Relatório Geral de Transações
4. Histórico de Importações
5. Relatório de Suspeitas de Fraude
6. Cadastrar, Consultar, Alterar e Deletar usuário do sistema

Nossa app esta disponibilizado para uso atráves do link:

    http://transactions-analyzer.herokuapp.com/

##### 1. Autenticação de Usuário

Ao acessar o link, você irá se deparar com a nossa tela de login.

![](readme/images/login.png)

Para realizar o acesso criamos as credenciais de acesso para você testar:

    Nome do Usuário: ADMIN
    Senha: 123999

    obs: Nesta tela de login na região inferior a imagem econtramos um link para
    recuperação ou troca de senha. Esta funcionalidade esta em desenvolvimento.

##### 2. Home Page (Navegação + Relatório Geral de Transalções)

Após realizar o login, o usuário é redirecionado para nossa home page

![img.png](readme/images/home-page.png)

Esta tela é composta por: dashboards, menu superior e uma barra de menu lateral

Dashboard:

    Os dados contidos na Dashboard são relativos as transações importadas no mês vigente,
    desta forma representando um relatório geral das trasações relativas ao mês corrente.

Menu Superior:

    Essa região contém, a esquerda, o icone para recolher ou mostrar o menu lateral,
    na região central fica o nome da tela, neste caso "Dashboard", a direita encontramos
    o botão para relizar o logout da aplicação.

Menu Lateral:

    Atrávez do menu de acesso lateral você pode navegar por nossa aplicação e acessar
    todas nossas funcionalidades. Ele é composto por essa opções:
    
    1. Dashboard
    2. Transações
        2.1 Importar
        2.2 Histórico
        2.3 Suspeitas
    3. Usuários
        3.1 Gerenciar

##### 3. Importar Transações

Para acessar a tela de importação você irá escolher a opção do menu lateral:

    Transações >  Importar

A tela de importação será carregada na home page

![](readme/images/import-transactions.png)

    Para escolher o arquivo desejado, clique na imagem com a seta apontada para cima.
    Ao escolher o arquivo a imagem irá mudar de uma seta para um V, o nome do arquivo
    irá aparece na tela e será habilitado um botão com nome "Enviar".
    Agora é só clicar em "Enviar"


##### 4. Histórico de Importações

Para acessar a tela de importação você irá escolher a opção do menu lateral:

    Transações >  Histórico

A tela de histórico será carregada na home page

![](readme/images/transaction-log.png)

Esta tela é composta por uma barra de pesquisa e logo abaixo uma tabela.

Barra de Pesquisa:

    Pra filtar os dados listados na tabela você pode digitar dentro deste campo a sua
    busca. A busca ocorre em todos os campos da tabela linha por linha.Caso não encontre
    o que você busca dentro de uma linha, ela será ocultada. 

Tabela:
    
    Esta tabela contém o log de transações realizadas. Cada arquivo importado através da
    opção Transações >  Importar é considerado um lote. Por exemplo: Um arquivo contendo
    transações do dia 01/06/2022 é considerado que essas transações fazem parte do lote
    01/06/2022. Dentro deste contexto esta tabela exibe o histórico de lotes importados.
    Caso deseje visualizar as transações contidas em um lote, você pode dar duplo click
    em uma das linha desta tabela. Ao realizar este procedimento uma nova tabela será
    exibida contendo as transações referente ao determinado lote da linha escolhida.

A nova tabela exibida será assim

![](readme/images/transaction-described.png)

    Esta nova tabela contém todas as transações contidas em um determinado lote. Podemos
    perceber que um botão com uma seta para esquerda foi habilitado logo acima da
    tabela. Este botão serve para retorna a tabela anterior, caso o usuário deseje
    verificar outro lote.

##### 5. Relatório de Suspeitas de Fraude

Para acessar a tela de importação você irá escolher a opção do menu lateral:

    Transações >  Suspeitas

A tela de Suspeitas será carregada na home page

![](readme/images/suspect-transactions.png)

Esta tela é composta por um campo para a escolha do mês e ano no canto superior esquerdo,
no canto superior direito temos 3 campos para marcar (Transações, Contas, Bancos)
e 3 tabelas (Transações, Contas, Bancos) no centro da página.

Campo para Escolher Mês e Ano

    Através deste campo o usuário poderá escolher qual mês e ano que deseja realizar a
    avaliação de suspeitas. Após selecionar a data desejada ele deverá clicar no botão
    com a imagem de lupa, localizado no mesmo campo. Os dados referentes a data escolhida
    irão preencher as tabelas

Campos para Marcar (Transações, Contas, Bancos)

    Estes campos servem para ocultar e mostrar as tabelas respecitvas aos seus nomes,
    como por exemplo: caso o usuário desmarque o campo com nome Transações a tabela
    com nome Transações irá sumir da tela, conforme imagem abaixo

![img.png](readme/images/suspect-transaction-checkbox-exemple.png)


##### 5. Cadastrar, Consultar, Alterar e Deletar usuário do sistema

Para acessar a tela de importação você irá escolher a opção do menu lateral:

    Usuário >  Gerenciar

A tela de Gerenciar Usuário será carregada na home page

![](readme/images/user.png)

Esta tela é composta por um campo de busca na parte supeior, um botão para adicionar
usuário na parte superior a direta do campo de busca, uma tabela e um formulário
oculto. Ao entrar nesta tela ela exibirá todos os usuários cadastrados
no sistema na tabela

Campo de Busca

    Pra filtar os dados listados na tabela você pode digitar dentro deste campo a sua
    busca. A busca ocorre em todos os campos da tabela linha por linha.Caso não encontre
    o que você busca dentro de uma linha, ela será ocultada.

Botão Adicionar Novo Usuário

    Este botão serve para a criação de um novo usuário. Ao ser clicado a tabela é
    ocultada e um formulário com os campos necessários para cadastrar o usuário é
    exibido. Conforme imagem abaixo
    
![](readme/images/new-user.png)    

Formulário Oculto

Este formulário possui em seu topo um campo para o nome do usuário, logo abaixo temos
o campo para o email, em baixo deste campo o campo status, um botão de salvar e um
botão de voltar

    Caso o usuário clique no botão para criar um novo usuário este formulário
    é exibido sem nenhum dos campos preenchidos, porém caso seja para alterar o usuário
    este formulário será carregado com as informações do usuário selecionado. Após
    preencher os campos ou edita-los, o usuário deverá clicar em salvar, mas caso
    deseje retorna a tabela de consulta de usuário ele poderá clicar em volta,
    fazendo isso as informações preenchidas não serão salvas no banco de dados

    obs 1: Ao cadastrar um novo usuário, o sistema enviará uma senha para o email
    informado. Caso o usuário deseje realizar a troca desta senha, ele poderá,
    através da página de login, clicar no link "Recuperar ou Trocar senha" e
    realizar a troca.

    obs 2: Todas as alterações realizadas são registradas em uma
    tabela de auditoria através de uma Trigger registada no banco SQL. Deste
    forma podemos auditar quaisquer mudanças realizas e identifcar o usuário
    responsável

Tabela

    Esta tabela contem as informações básicas do usuário. Caso deseje alterar um deste
    registro, você deverá realizar um duplo clique na linha desejad. Desta forma
    a tabela irá ser ocultado e o formulário de usuário será exibido com as
    informações referentes a linha escolhida.


### 2. Clonando Repositório:
    
    Seção do README não disponível neste momento 

### 3. Consumir nossa API:
    
    Seção do README não disponível neste momento 