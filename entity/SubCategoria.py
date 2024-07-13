from django.db import models
import Categoria

class SubCategoria:

    class Meta:
        db_table = "tb_sub_categoria"

    id = models.CharField(max_length=256, db_column="id_sub_categoria", primary_key=True)
    descricao = models.CharField(max_length=256, db_column="desc_sub_categoria")
    categoria = models.ForeignKey(Categoria, db_column="id_categoria")

    def __init__(self, id, descricao, categoria):
        self.id = id
        self.descricao = descricao
        self.categoria = categoria

    def set_id(self, id):
        self.id = id

    def set(self, descricao):
        self.descricao = descricao

    def set(self, categoria):
        self.categoria = categoria

    def get_id(self):
        return self.id

    def get_descricao(self):
        return self.descricao

    def get_categoria(self):
        return self.categoria