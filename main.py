from lib.cart import *
from lib.product import *
from lib.user import *
from lib.interface import *

def main():
    clear()
    while True:
        opt = main_menu()
        match opt:
            case "1":
                clear()
            case "2":
                clear()
            case "3":
                clear()
            case "0":
                clear()
                print("O usuário encerrou o sistema.\n")
                break
            case _:
                clear()
                print("Opção inválida.\n")

if __name__ == "__main__":
    main()