class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(name=data['name'], email=data['email'], password=data['password'])

def login(users):
    print("=== SHOPPING ===")
    email = input("Email: ")
    password = input("Senha: ")

    for user in users:
        if email == user.email and password == user.password:
            return user
    
    return None

def register():
    print("=== SHOPPING ===")
    name = input("Digite seu nome: ")
    email = input("Digite seu email ")
    password = input("Crie sua senha: ")
    confirm = input("Digite sua senha novamente: ")

    if confirm != password:
        return False

    user = User(name, email, password)

    return user
