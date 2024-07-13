class Sub_movimentacao:
    def __init__(self, id, data_prev_sub_movimentacao, data_real_sub_movimentacao, valor_sub_movimentacao, id_forma_pgto, id_movimentacao):
        self.id = id
        self.data_prev_sub_movimentacao = data_prev_sub_movimentacao
        self.data_real_sub_movimentacao = data_real_sub_movimentacao
        self.valor_sub_movimentacao = valor_sub_movimentacao
        self.id_forma_pgto = id_forma_pgto
        self.id_movimentacao = id_movimentacao


    #GET
    def get_id(self):
        return self.id

    def get_data_prev_sub_movimentacao(self):
        return self.data_prev_sub_movimentacao

    def get_data_real_sub_movimentacao(self):
        return self.data_real_sub_movimentacao
    
    def get_id_forma_pgto(self):
        return self.id_forma_pgto
    
    def get_id_movimentacao(self):
        return self.id_movimentacao



    #SET
    def set_id(self, id):
        self.id = id

    def set_data_prev_sub_movimentacao(self, data_prev_sub_movimentacao):
        self.data_prev_sub_movimentacao = data_prev_sub_movimentacao

    def set_data_real_sub_movimentacao(self, data_real_sub_movimentacao):
        self.data_real_sub_movimentacao = data_real_sub_movimentacao

    def set_valor_sub_movimentacao(self, valor_sub_movimentacao):
        self.valor_sub_movimentacao = valor_sub_movimentacao

    def set_id_movimentacao(self, id_movimentacao):
        self.id_movimentacao = id_movimentacao