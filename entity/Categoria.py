from django.db import models

class Categoria(models.Model):
    class Meta:
        db_table = "tb_categoria"

    id = models.CharField(max_length=256, db_column="id_categoria", primary_key=True)
    descricao = models.CharField(max_length=50, db_column="desc_categoria")

    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id
    
    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_descricao(self):
        return self.descricao