class Transacao:

    def __init__(self, id, descricao, data_transacao, usuario, categoria):
        self.id = id
        self.descricao = descricao
        self.data_transacao = data_transacao
        self.usuario = usuario
        self.categoria = categoria

    def set_id(self, id):
        self.id = id
    
    def set_descricao(self, descricao):
        self.descricao = descricao
    
    def set_data_transacao(self, data_transacao):
        self.data_transacao = data_transacao
    
    def set_usuario(self, usuario):
        self.usuario = usuario
    
    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_id(self):
        return self.id
    
    def get_descricao(self):
        return self.descricao
    
    def get_data_transacao(self):
        return self.data_transacao
    
    def get_usuario(self):
        return self.usuario
    
    def get_categoria(self):
        return self.categoria
    