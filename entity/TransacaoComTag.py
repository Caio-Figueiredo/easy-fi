class TransacaoComTag:

    def __init__(self, id, transacao):
        self.id = id
        self.transacao = transacao

    def get_id(self):
        return self.id

    def get_transacao(self):
        return self.transacao

    def set_id(self, id):
        self.id = id

    def set_transacao(self, transacao):
        self.transacao = transacao