class User():
    def __init__(self, name, username, email, password, admin):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.admin = admin

    def to_dict(self):
        return {
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "admin": self.admin
        }

    @classmethod
    def from_dict(cls, data):
        return cls(name=data['name'], username=data['username'], email=data['email'], password=data['password'], admin=data['admin'])

def login(users):
    print("=== SHOPPING ===")
    username = input("Nome de usuário: ")
    password = input("Senha: ")

    for user in users:
        if username == user.username and password == user.password:
            return user
    
    return None

def register():
    print("=== SHOPPING ===")
    name = input("Digite seu nome: ")
    username = input("Crie seu nome de usuário: ")
    email = input("Digite seu email ")
    password = input("Crie sua senha: ")
    confirm = input("Digite sua senha novamente: ")
    admin = False

    if confirm != password:
        return False

    user = User(name, username, email, password, admin)

    return user
