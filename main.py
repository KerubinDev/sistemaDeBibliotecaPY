class Livro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    def adicionar(self, biblioteca):
        biblioteca.adicionar__livro(self)

    def buscar(self, termo):
        return termo.lower() in self.__titulo.lower() or termo.lower in self.__autor.lower()
    
    def emprestar(self, usuario):
        if self.__disponivel:
            self.__disponivel = False

            usuario.adicionar_livro(self)
            print(f"Livro '{self.__titulo}' emprestado para {usuario.nome}.")
        else:
            print(f"livro '{self.__titulo}' não está disponivel.")

    def devolver(self, usuario):
        self.__disponivel = True
        usuario.remover_livro(self)
        print(f"Livro '{self.__titulo}' devolvido por {usuario.nome}.")

    @property
    def titulo(self):
        return self.__titulo
    @property
    def titulo(self):
        return self.__titulo
    @property
    def autor(self):
        return self.__autor
    @property
    def isbn(self):
        return self.__isbn
    
class Autor:
    def __init__(self, nome, nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nome

    @property
    def nome(self):
        return self.__nome
    @property
    def nacionalidade(self):
        return self.__nacionalidade
    
class Usuario:
    def __init__(self, nome, id_usuario  ):