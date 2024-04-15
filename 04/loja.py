
class Usuario:
    def __init__(self, nome, apelido, senha):
        self.nome = nome
        self.apelido = apelido
        self.senha = senha
        self.email = nome + apelido

class Cliente(Usuario):
    def __init__(self, nome, apelido, senha, endereco):
        super().__init__(nome, apelido, senha)
        self.endereco = endereco

class Funcionario(Usuario):
    def __init__(self, nome, apelido, senha, cargo):
        super().__init__(nome, apelido, senha)
        self.cargo = cargo

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Pagamento:
    def __init__(self, cliente, produto, metodo_pagamento):
        self.cliente = cliente
        self.produto = produto
        self.metodo_pagamento = metodo_pagamento

class Entrega:
    def __init__(self, cliente, produto, endereco_entrega):
        self.cliente = cliente
        self.produto = produto
        self.endereco_entrega = endereco_entrega
print(Usuario)