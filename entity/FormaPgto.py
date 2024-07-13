from django.db import models
import datetime

class FormaPgto(models.Model):
    class Meta:
        db_table = "tb_forma_pgto"

    id = models.CharField(max_length=256, db_column = "id_forma_pgto", primary_key=True)
    descricao = models.CharField(max_length=256, db_column = "desc_froma_pgto")
    current_date = models.TimeField(db_column="registro_evento_criacao")

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