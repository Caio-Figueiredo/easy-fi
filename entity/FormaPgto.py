class FormaPgto:

    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

    def get_id(self):
        return self.id

    def get_descricao(self):
        return self.descricao

    def set_id(self, id):
        self.id = id

    def set_descricao(self, descricao):
        self.nome = descricao