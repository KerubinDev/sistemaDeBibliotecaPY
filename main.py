class Livro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponivel = True

    def adicionar(self, biblioteca):
        biblioteca.adicionar_livro(self)

    def buscar(self, termo):
        return termo.lower() in self.__titulo.lower() or termo.lower() in self.__autor.lower()

    def emprestar(self, usuario):
        if self.__disponivel:
            self.__disponivel = False
            usuario.adicionar_livro(self)
            print(f"Livro '{self.__titulo}' emprestado para {usuario.nome}.")
        else:
            print(f"Livro '{self.__titulo}' não está disponível.")

    def devolver(self, usuario):
        self.__disponivel = True
        usuario.remover_livro(self)
        print(f"Livro '{self.__titulo}' devolvido por {usuario.nome}.")

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def isbn(self):
        return self.__isbn

    @property
    def disponivel(self):
        return self.__disponivel


class Autor:
    def __init__(self, nome, nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nacionalidade

    @property
    def nome(self):
        return self.__nome

    @property
    def nacionalidade(self):
        return self.__nacionalidade


class Usuario:
    def __init__(self, nome, id_usuario):
        self.__nome = nome
        self.__id_usuario = id_usuario
        self.__livros_emprestados = []

    def adicionar_livro(self, livro):
        self.__livros_emprestados.append(livro)

    def remover_livro(self, livro):
        self.__livros_emprestados.remove(livro)

    @property
    def nome(self):
        return self.__nome

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def livros_emprestados(self):
        return self.__livros_emprestados


class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__usuarios = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def adicionar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        print(f"Usuário '{usuario.nome}' adicionado ao sistema.")

    def buscar_livros(self, termo):
        resultados = [livro for livro in self.__livros if livro.buscar(termo)]
        return resultados

    @property
    def livros(self):
        return self.__livros

    @property
    def usuarios(self):
        return self.__usuarios


# Exemplo de uso:

biblioteca = Biblioteca()

autor1 = Autor("George Orwell", "Britânico")
livro1 = Livro("1984", autor1.nome, "123456789")
livro1.adicionar(biblioteca)

usuario1 = Usuario("João Silva", "001")
biblioteca.adicionar_usuario(usuario1)

resultados_busca = biblioteca.buscar_livros("Orwell")
for livro in resultados_busca:
    print(f"Livro encontrado: {livro.titulo}, Autor: {livro.autor}")

livro1.emprestar(usuario1)
livro1.devolver(usuario1)
