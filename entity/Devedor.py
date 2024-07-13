from django.db import models
import datetime

class Devedor:
    class Meta:
        db_table = "tb_devedor"

    id = models.CharField(max_length=256, primary_key=True, db_column="id_devedor")
    nome = models.CharField(max_length=256, db_column="nome_devedor")
    create_current_date = models.TimeField(db_column="registro_evento_criacao") 
    

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome