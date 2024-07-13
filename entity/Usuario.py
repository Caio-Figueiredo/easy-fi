class Usuario:

    def __init__(self, id, nome, sobrenome, email, senha):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_sobrenome(self):
        return self.sobrenome

    def get_email(self):
        return self.email

    def get_senha(self):
        return self.senha    

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def set_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def set_email(self, email):
        self.email = email

    def set_senha(self, senha):
        self.senha = senha