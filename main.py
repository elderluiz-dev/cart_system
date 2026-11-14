from lib.cart import *
from lib.product import *
from lib.user import *
from lib.interface import *
import json

def main():
    try:
        with open("users.json", "r", encoding='utf-8') as file:
            data = json.load(file)
            users = [User.from_dict(user) for user in data]

    except FileNotFoundError:
        users = []

    clear()
    method = initial()
    match method:
        case "1":
            clear()
            user = login(users)
            if user == None:
                print("Usuário não encontrado.\n")
                return
                
        case "2":
            clear()
            new_user = register()
            while new_user == False:
                print("As senhas não conhecidem.\n")
                new_user = register()

            users.append(new_user)
            user = new_user

        case "0":
            clear()
            print("O usuário encerrou o programa.\n")
            return
        case _:
            clear()
            print("Opção inválida\n")

    clear() 
    print(f"Bem vindo {user.name.upper()}!")
    while True:
        opt = main_menu()
        match opt:
            case "1":
                clear()


            case "2":
                clear()


            case "3":
                clear()


            case "4":
                clear()
                while True:
                    admc = admin_menu()
                    match admc:
                        case "1":
                            clear()
                        case "2":
                            clear()
                        case "0":
                            clear()
                            break
                        case _:
                            clear()
                            print("Opção inválida.\n")


            case "0":
                clear()
                with open("users.json", "w", encoding='utf-8') as file:
                    json.dump([user.to_dict() for user in users], file, indent=4, ensure_ascii=False)

                print("O usuário encerrou o sistema.\n")
                break


            case _:
                clear()
                print("Opção inválida.\n")

if __name__ == "__main__":
    main()
