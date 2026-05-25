# Sistema CRUD em Python (Modularizado)

Este é um sistema simples de **CRUD** (Create, Read, Update, Delete) desenvolvido em Python utilizando o banco de dados **SQLite**. O projeto foi estruturado de forma modular (dividido em arquivos) para seguir as boas práticas de desenvolvimento, separando a lógica de banco de dados da interface do usuário.

## 🛠️ Tecnologias Utilizadas

*   **Python 3.x**
*   **SQLite** (Banco de dados relacional leve, nativo do Python)

## 📁 Estrutura do Projeto

O projeto é dividido nos seguintes arquivos:

*   `database.py`: Gerencia a conexão com o banco de dados e a criação automatizada da tabela.
*   `crud.py`: Contém as funções com as regras de negócio e operações do banco de dados (inserir, listar, atualizar e deletar).
*   `main.py`: Interface de linha de comando (CLI) que interage com o usuário.

## 🚀 Como Executar o Projeto

### Pré-requisitos
Você só precisa ter o **Python 3** instalado na sua máquina. Não é necessário instalar nenhuma biblioteca externa (como `pip install`), pois o SQLite já vem incluso no Python.

### Passo a Passo

1.  **Clone ou baixe** os arquivos do projeto para uma pasta no seu computador.
2.  Abra o seu terminal (ou prompt de comando) e navegue até a pasta do projeto:
```bash
    cd /caminho/para/a/pasta/do/projeto
    ```
3.  Execute o arquivo principal:
```bash
    python main.py
    ```

## 📋 Funcionalidades

O sistema roda diretamente no terminal e permite as seguintes ações:

1.  **Cadastrar Usuário (Create):** Solicita Nome, Email e Idade. O sistema valida se o e-mail já existe para evitar duplicidade.
2.  **Listar Usuários (Read):** Exibe todos os usuários cadastrados em uma tabela formatada no terminal.
3.  **Atualizar Usuário (Update):** Permite alterar os dados de um usuário existente buscando-o pelo seu ID.
4.  **Deletar Usuário (Delete):** Remove permanentemente um usuário do banco de dados através do seu ID.

## 🗃️ O Banco de Dados

Ao rodar o projeto pela primeira vez, um arquivo chamado `sistema.db` será criado automaticamente na raiz da pasta. Ele guardará todas as informações de forma persistente (você pode fechar o terminal e abrir novamente que os dados continuarão salvos).
