import Transacao
from django.db import models

class InvestimentoFinanceiro(models.Model):
    class Meta:
        db_table = "tb_investimento_financeiro"

    id = models.CharField(max_length=256, primary_key=True, db_column="id_investimento_financeiro")
    nome_corretora = models.CharField(max_length=256, db_column="nome_corretora_investimento_financeiro")
    transacao = models.ForeignKey(Transacao, db_column="id_transacao") 
    

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