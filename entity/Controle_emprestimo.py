class Controle_emprestimo:

    def __init__(self, id_sub_mov, id_devedor):
        self.id_devedor = id_devedor
        self.id_sub_mov = id_sub_mov
    
    def set_id_devedor(self, id_devedor):
        self.id_devedor = id_devedor
    
    def set_id_sub_mov(self, id_sub_mov):
        self.id_sub_mov = id_sub_mov
    
    def get_id_sub_mov(self):
        return self.id_devedor
    
    def get_id_sub_mov(self):
        return self.id_sub_mov