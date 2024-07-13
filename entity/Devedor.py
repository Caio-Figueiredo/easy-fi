class Devedor:

    def __init__(self, id, nome_do_devedor):
        self.id = id
        self.nome_do_devedor = nome_do_devedor

    def get_id(self):
        return self.id

    def get_nome_do_devedor(self):
        return self.nome_do_devedor

    def set_id(self, id):
        self.id = id

    def set_nome_do_devedor(self, nome_do_devedor):
        self.nome_do_devedor = nome_do_devedor