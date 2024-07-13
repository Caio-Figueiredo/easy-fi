class InvestimentoFinanceiro:

    def __init__(self, id, nome_corretora, transacao):
        self.id = id
        self.nome_corretora = nome_corretora
        self.transacao = transacao

    def get_id(self):
        return self.id

    def get_nome_corretora(self):
        return self.nome_corretora
    
    def get_transacao(self):
        return self.transacao

    def set_id(self, id):
        self.id = id

    def set_nome_corretora(self, nome_corretora):
        self.nome_corretora = nome_corretora

    def set_transacao(self, transacao):
        self.transacao = transacao