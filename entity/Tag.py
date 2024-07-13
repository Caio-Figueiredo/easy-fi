from django.db import models

class Tag(models.Model):
    class Meta:
        db_table = "tb_tag_transacao"

    id = models.CharField(max_length=256,primary_key=True, db_column="id_tag_transacao")
    descricao = models.CharField(max_length=256, db_column="desc_tag_transacao")
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
        self.descricao = descricao