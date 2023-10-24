class Produto:
    # Inicialização da classe
    def __init__(self, id_produto, nome, descricao, preco, estoque):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

    # Método para exibir informações do produto
    def exibir_produto(self):
        print(f"ID: {self.id_produto}")
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Estoque: {self.estoque} unidades")

    # Método para atualizar informações do produto
    def atualizar_produto(self, nome, descricao, preco, estoque):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
