class Livro:
    def __init__(self, nome, autor, ano, preco, qntd):
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.preco = preco 
        self.qntd = qntd

livro_1 = Livro('Livro 1', 'Iago', 2024, 15.99, 10)
livro_2 = Livro('Livro 1', 'Iago', 2024, 15.99, 10)

print('livro 1 : ', livro_1.nome,',', livro_1.autor,',', livro_1.ano,',', livro_1.preco,',', livro_1.qntd)