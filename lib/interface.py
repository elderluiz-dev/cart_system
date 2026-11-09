def clear():
    print('\033[H\033[2J', end='')

def main_menu():
    print("=== SHOPPING ===")
    print("1. Listar produtos")
    print("2. Configurações do usuário")
    print("3. Carrinho")
    print("0. Sair")
    c = input("> ")

    return c