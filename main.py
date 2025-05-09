import os
from user import add_user, users

op = ""
re = ""
def main():
    print("Teste de função de registro de usuário")
    
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def register_user(username: str = "", password: str = ""):
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")
    add_user(username, password)
    print(f"Usuário {username} registrado com sucesso!")
    
def list_users(users: list = users):
    if not users:
        print("Nenhum usuário registrado.")
    else:
        print("Usuários registrados:")
        for i, user in enumerate(users, start=1):
            print(f"{i}. {user.username}")

def clear_users():
    while True:
        limpar_tela()
        if not users:
            print("Nenhum usuário registrado.")
            break
        else:
            print("usuários registrados:")
            for i, user in enumerate(users, start=1):
                print(f"{i}. {user.username}")
            re =input("Digite o número do usuário que deseja remover ou 'clear' para limpar toda a lista.\n0 para cancelar\n ")
            if re == "0":
                print("Operação cancelada.")
                break
            elif re == "clear":
                for user in users:
                    users.remove(user)
                print("Lista de usuários limpa com sucesso!")
                break
            else:
                try:
                    index = int(re) - 1
                    if 0 <= index < len(users):
                        removed_user = users.pop(index)
                        print(f"Usuário {removed_user.username} removido com sucesso!")
                        break
                    else:
                        print("Número inválido. Tente novamente.")
                        input("\nPressione Enter para continuar...")
                except ValueError:
                    print("Entrada inválida. tente novamente.")
                    input("\nPressione Enter para continuar...")
            
        
def main_menu():            
    while True:
        limpar_tela()
        main()
        op = input("Digite 1 para registrar um novo usuário, 2 para ver a lista de usuários ou 3 para excluir um usuário.\n0 para sair: ")
        match op:
            case "1":
                limpar_tela()
                register_user()
            case "2":
                limpar_tela()
                list_users()
                input("\nPressione Enter para continuar...")
            case "3":
                
                clear_users()
                input("\nPressione Enter para continuar...")
            case "0":
                print("Saindo do programa.")
                break
            case _:
                limpar_tela()
                print("Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main_menu()