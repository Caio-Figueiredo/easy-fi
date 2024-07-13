from django.db import models
import Transacao

class Movimentacao(models.Model):

    class Meta:
        db_table = "tb_categoria"

    id = models.CharField(max_length=256, db_column="id_movimentacao", primary_key=True)
    num_parc = models.IntegerField(max_length=256, db_column="num_parcela_atual_movimentacao")
    transacao = models.ForeignKey(Transacao, on_delete=models.CASCADE, db_column="id_transacao")

    def __init__(self, id, num_parc, transacao):
        self.id = id
        self.num_parc = num_parc
        self.transacao = transacao

    def get_id(self):
        return self.id

    def get_num_parc(self):
        return self.num_parc

    def get_transacao(self):
        return self.transacao

    def set_id(self, id):
        self.id = id

    def set_num_parc(self, num_parc):
        self.num_parc = num_parc

    def set_transacao(self, transacao):
        self.transacao = transacao