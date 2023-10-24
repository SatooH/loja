import pickle

class Produto:
    def __init__(self, id, nome, descricao, preco, estoque):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nDescrição: {self.descricao}\nPreço: R${self.preco:.2f}\nEstoque: {self.estoque} unidades"

    def atualizar(self, nome, descricao, preco, estoque):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

class Catalogo:
    def __init__(self):
        self.catalogo = []
        self.proximo_id = 1

    def adicionar_produto(self, nome, descricao, preco, estoque):
        produto = Produto(self.proximo_id, nome, descricao, preco, estoque)
        self.catalogo.append(produto)
        self.proximo_id += 1
        print("Produto adicionado com sucesso!")

    def listar_produtos(self):
        if not self.catalogo:
            print("O catálogo está vazio.")
            return

        print("Lista de Produtos:")
        for produto in self.catalogo:
            print(produto.nome)

        print("\n")

    def atualizar_produto(self, id, nome, descricao, preco, estoque):
        for produto in self.catalogo:
            if produto.id == id:
                produto.atualizar(nome, descricao, preco, estoque)
                print("Produto atualizado com sucesso!")
                return
        print("Produto não encontrado.")

    def excluir_produto(self, id):
        for produto in self.catalogo:
            if produto.id == id:
                self.catalogo.remove(produto)
                print("Produto excluído com sucesso!")
                return
        print("Produto não encontrado.")

    def salvar_catalogo(self, arquivo):
        with open(arquivo, 'wb') as file:
            pickle.dump(self.catalogo, file)
        print("Catálogo salvo com sucesso!")

    def carregar_catalogo(self, arquivo):
        try:
            with open(arquivo, 'rb') as file:
                self.catalogo = pickle.load(file)
            print("Catálogo carregado com sucesso!")
        except FileNotFoundError:
            print("Arquivo de catálogo não encontrado.")

def main():
    catalogo = Catalogo()

    while True:
        print("\nSistema de Gerenciamento de Catálogo de Produtos")
        print("1. Adicionar um novo produto")
        print("2. Listar todos os produtos")
        print("3. Atualizar um produto")
        print("4. Excluir um produto")
        print("5. Salvar catálogo em arquivo")
        print("6. Carregar catálogo de arquivo")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do produto: ")
            descricao = input("Descrição do produto: ")
            preco = float(input("Preço do produto: "))
            estoque = int(input("Quantidade em estoque: "))
            catalogo.adicionar_produto(nome, descricao, preco, estoque)

        elif escolha == "2":
            catalogo.listar_produtos()

        elif escolha == "3":
            id = int(input("ID do produto a ser atualizado: "))
            nome = input("Novo nome do produto: ")
            descricao = input("Nova descrição do produto: ")
            preco = float(input("Novo preço do produto: "))
            estoque = int(input("Nova quantidade em estoque: "))
            catalogo.atualizar_produto(id, nome, descricao, preco, estoque)

        elif escolha == "4":
            id = int(input("ID do produto a ser excluído: "))
            catalogo.excluir_produto(id)

        elif escolha == "5":
            nome_arquivo = input("Digite o nome do arquivo para salvar o catálogo: ")
            catalogo.salvar_catalogo(nome_arquivo)

        elif escolha == "6":
            nome_arquivo = input("Digite o nome do arquivo para carregar o catálogo: ")
            catalogo.carregar_catalogo(nome_arquivo)

        elif escolha == "7":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
