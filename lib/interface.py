def clear():
    print('\033[H\033[2J', end='')

def main_menu():
    print("=== SHOPPING ===")
    print("1. Listar produtos")
    print("2. Configurações do usuário")
    print("3. Carrinho")
    print("4. Modo administrador")
    print("0. Sair")
    c = input("> ")

    return c

def admin_menu():
    print("=== SHOPPING - ADMIN ===")
    print("1. Editar produtos")
    print("2. Editar usuários")
    print("0. Sair do modo admin")
    c = input("> ")

    return c

def initial():
    print("=== SHOPPING ===")
    print("1. Entrar")
    print("2. Fazer cadastro")
    print("0. Sair")
    c = input("> ")

    return c
