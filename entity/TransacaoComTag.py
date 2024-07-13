from django.db import models
import Tag
import Transacao

class TransacaoComTag(models.Model):
    class Meta:
        db_table = "tb_transacoes_com_tag"
    
    id = models.ForeignKey(Tag,db_column = "id_tag_transacao")
    transacao = models.ForeignKey(Transacao, db_column = "id_transacao")


    
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