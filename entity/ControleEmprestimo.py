from django.db import models
import Devedor

class ControleEmprestimo(models.Model):
    class Meta:
        db_table = "tb_controle_emprestimo"

    id = models.CharField(max_length=256, primary_key=True, db_column="id_sub_movimentacao")
    devedor = models.ForeignKey(Devedor, db_column="id_devedor")
    

    def __init__(self, id, devedor):
        self.id = id
        self.devedor = devedor
    
    def set_devedor(self, devedor):
        self.devedor = devedor
    
    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.devedor
    
    def get_id(self):
        return self.id