from django.db import models
import Transacao

class ResgateInvestimentoFinanceiro(models.Model):
    class Meta:
        db_table = "tb_resgate_investimento_financeiro"

    id = models.CharField(max_length=256, primary_key=True, db_column="id_resgate_investimento_financeiro")
    transacao = models.ForeignKey(Transacao, db_column="id_transacao")

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