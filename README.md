# Trabalho Prático 1 - Engenharia de Software

## Escopo do sistema:

  Objetivo:<br>
    > Criar um sistema de crédito vinculado à carteirinha de identificação da UFMG para ser utilizado nos restaurantes universitários dos campos da UFMG pelos alunos, afim de acelerar a forma de pagamento, diminuir a fila desses restaurantes e diminuir os problemas relacionados a troco.<br>
  
  Principais features:<br>
    > Controle de login de usuário;<br>
    > Painel de usuário nível 0, com informações de crédito da conta e dados do usuário;<br>
    > Painel de administrador nível 1, sendo este uma pessoa responsável pela inserção de crédito em contas de usuários nível 0;<br>
    > Painel de administrador nível 2, sendo este capaz de monitorar o fluxo de pessoas dos restaurantes universitários analisandos as informações relevantes do sistema;<br>
    

## Membros da equipe e papel:

  Bernardo Franco Tormin (2019027350) - Função: Backend<br>
  João Pedro Maduro Menezes (2019027679) - Função: Frontend<br>
  Leonel Siqueira Martinez Palhares (2019070094) - Função: Frontend<br>
  Vinícius Guimarães Silva (2019028187) - Função: Backend<br>

## Tecnologias:

  Linguagem:<br>
    > Python;<br>
    > Dart.<br>

  Frameworks:<br>
    > Flutter;<br>
    > Flask;<br>
    > Dash.<br>

  BD:<br>
    > PostgreSQL;<br>

## Link do planejamento das sprints:

"https://closed-wildebeest-89c.notion.site/ac76b3ee527a4a74b01de11c9d4c1a2c?v=750c04a87b5e468da4b6700f3deab351"

## Scrum:

| Backlog do Produto                                               | Backlog da Sprint                                               |
|:------------------------------------------------------------------:|:--------------------------------------------------------------:|
| Como usuário nível 2, gostaria de ver o fluxo de clientes em um determinado período. | Como usuário nível 0, gostaria de ver o saldo da minha conta no sistema. |
| Como usuário nível 0, gostaria de receber um e-mail avisando que só tenho uma ficha de alimentação restante. | Como usuário nível 1, gostaria de fazer o cadastro de um cliente. |
| Como usuário nível 2, gostaria de gerar gráficos a partir dos dados disponibilizados. | Como usuário nível 1, gostaria de adicionar crédito em uma conta. |
| Como usuário nível 2, gostaria de obter estatísticas sobre os dados coletados. | Como usuário nível 2, gostaria de ver os dados financeiros diários obtidos pelos RUs. |
| Como usuário nível 0, gostaria de receber um e-mail de confirmação de crédito do depósito. | Como usário nível 0, gostaria de almoçar com o meu saldo da conta. |
| Como usuário nível 0, gostaria de poder ver comentários diários sobre a comida oferecida por cada RU. |  |
| Como usuário nível 1, gostaria de receber, na própria plataforma, a informação de confirmação que o crédito foi depositado ou não com sucesso. | |
| Como usuário nível 2, gostaria de ter um feedback simples (se a comida do dia estava boa ou não), daqueles que frequentaram os RUs. | |

## Tasks:

  1.  Como usuário nível 0, gostaria de ver o saldo da minha conta no sistema.
        > Página de login: João;<br>
        > Acessar o botão saldo: João;<br>
        > POST request do frontend pra obter o saldo: Bernardo;<br>
        > Payload ECDSA encrypt ou signature: Vinícius;<br>
        > Lógica no backend para responder o POST request: Leonel.<br>

  2.  Como usuário nível 1, gostaria de fazer o cadastro de um cliente.
        > Criar uma tabela de usuários nível 0: Leonel;<br>
        > Criar uma interface para o usuário nível 1: João;<br>
        > Adicionar opção cadastrar usuário na interface do usuário nível 1: João;<br>
        > Obter dados digitados no cadastro do usuário nível 0: Bernardo;<br>
        > Alocar o usuário cadastrado no banco de dados: Bernardo.<br>

  3.  Como usuário nível 1, gostaria de adicionar crédito em uma conta.
        > Adicionar a opção “Adicionar crédito” na interface do usuário nível 1: João;<br>
        > Atualizar estado do saldo daquele cujo foi feito o deposito: Vinícius.<br>

  4.  Como usuário nível 2, gostaria de ver os dados financeiros diários obtidos pelos RUs.
        > Criar interface de usuário nível 2: João;<br>
        > Criar uma tabela para armazenar os clientes que frequenta o RU: Leonel;<br>
        > Inserir cliente na tabela quando este frequentar o RU: Vinícius;<br>
        > Analisar os dados desta tabela e retornar informações desejadas: Leonel.<br>

  5.  Como usário nível 0, gostaria de almoçar com o meu saldo da conta.
        > Criar lógica de subtrair o saldo do usuário: Vinícius;<br>
        > Atualizar saldo do usuário no banco de dados: Leonel.<br>
