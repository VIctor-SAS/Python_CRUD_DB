import crud
from database import inicializar_banco

def exibir_menu():
    print("\n" + "="*30)
    print("       CADASTRO DE USUÁRIOS       ")
    print("="*30)
    print("1. Cadastrar Usuário")
    print("2. Listar Usuários")
    print("3. Atualizar Usuário")
    print("4. Deletar Usuário")
    print("5. Sair")
    print("="*30)

def menu_cadastrar():
    nome = input("Nome: ")
    email = input("Email: ")
    try:
        idade = int(input("Idade: "))
        if crud.criar_usuario(nome, email, idade):
            print(f"\n[SUCESSO] Usuário '{nome}' cadastrado!")
        else:
            print(f"\n[ERRO] O email '{email}' já está cadastrado.")
    except ValueError:
        print("\n[ERRO] Idade precisa ser um número inteiro.")

def menu_listar():
    usuarios = crud.ler_usuarios()
    if not usuarios:
        print("\n[AVISO] Nenhum usuário encontrado.")
        return
    
    print("\n=== LISTA DE USUÁRIOS ===")
    print(f"{'ID':<5} | {'Nome':<20} | {'Email':<30} | {'Idade':<5}")
    print("-" * 65)
    for u in usuarios:
        print(f"{u[0]:<5} | {u[1]:<20} | {u[2]:<30} | {u[3]:<5}")

def menu_atualizar():
    try:
        id_usuario = int(input("Digite o ID do usuário que deseja atualizar: "))
        nome = input("Novo Nome: ")
        email = input("Novo Email: ")
        idade = int(input("Nova Idade: "))
        
        resultado = crud.atualizar_usuario(id_usuario, nome, email, idade)
        
        if resultado == "sucesso":
            print(f"\n[SUCESSO] Usuário ID {id_usuario} atualizado!")
        elif resultado == "nao_encontrado":
            print(f"\n[ERRO] Usuário com ID {id_usuario} não encontrado.")
        elif resultado == "email_duplicado":
            print(f"\n[ERRO] O email '{email}' já está em uso por outro usuário.")
            
    except ValueError:
        print("\n[ERRO] ID e Idade precisam ser números inteiros.")

def menu_deletar():
    try:
        id_usuario = int(input("Digite o ID do usuário que deseja deletar: "))
        if crud.deletar_usuario(id_usuario):
            print(f"\n[SUCESSO] Usuário ID {id_usuario} removido!")
        else:
            print(f"\n[ERRO] Usuário com ID {id_usuario} não encontrado.")
    except ValueError:
        print("\n[ERRO] ID precisa ser um número inteiro.")

def main():
    inicializar_banco() 
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            menu_cadastrar()
        elif opcao == "2":
            menu_listar()
        elif opcao == "3":
            menu_atualizar()
        elif opcao == "4":
            menu_deletar()
        elif opcao == "5":
            print("\nSaindo... Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()