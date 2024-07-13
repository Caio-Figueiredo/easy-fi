class Categoria:

    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id
    
    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_descricao(self):
        return self.descricao