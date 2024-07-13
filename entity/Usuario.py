class Usuario:

    def __init__(self, id, nome, sobrenome, email, senha):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getSobrenome(self):
        return self.sobrenome

    def getEmail(self):
        return self.email

    def getSenha(self):
        return self.senha    

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setSobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def setEmail(self, email):
        self.email = email

    def setSenha(self, senha):
        self.senha = senha