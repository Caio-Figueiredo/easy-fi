from django.db import models
import Usuario
import Categoria
import SubCategoria

class Transacao(models.Model):

    class Meta:
        db_table = "tb_transacao"

    id = models.CharField(max_length=256, db_column="id_transacao", primary_key=True)
    descricao = models.CharField(max_length=256, db_column="desc_transacao")
    data_transacao = models.DateField(max_length=256, db_column="data_transacao")
    usuario = models.ForeignKey(Usuario, db_column="id_usuario")
    categoria = models.ForeignKey(Categoria, db_column="id_categoria")
    sub_categoria = models.ForeignKey(SubCategoria, db_column="id_sub_categoria")

    def __init__(self, id, descricao, data_transacao, usuario, categoria, sub_categoria):
        self.id = id
        self.descricao = descricao
        self.data_transacao = data_transacao
        self.usuario = usuario
        self.sub_categoria = sub_categoria

    def set_id(self, id):
        self.id = id
    
    def set_descricao(self, descricao):
        self.descricao = descricao
    
    def set_data_transacao(self, data_transacao):
        self.data_transacao = data_transacao
    
    def set_usuario(self, usuario):
        self.usuario = usuario
    
    def set_categoria(self, categoria):
        self.categoria = categoria

    def set_sub_categoria(self, sub_categoria):
        self.sub_categoria = sub_categoria

    def get_id(self):
        return self.id
    
    def get_descricao(self):
        return self.descricao
    
    def get_data_transacao(self):
        return self.data_transacao
    
    def get_usuario(self):
        return self.usuario
    
    def get_categoria(self):
        return self.categoria

    def get_sub_categoria(self):
        return self.sub_categoria
    