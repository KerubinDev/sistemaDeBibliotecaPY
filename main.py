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


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\nMenu de Gerenciamento da Biblioteca")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Adicionar Usuário")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            isbn = input("Digite o ISBN do livro: ")
            novo_livro = Livro(titulo, autor, isbn)
            novo_livro.adicionar(biblioteca)
            print(f'Livro "{titulo}" adicionado à biblioteca.')

        elif escolha == "2":
            termo = input("Digite o termo para busca: ").lower()
            resultados = biblioteca.buscar_livros(termo)

            if resultados:
                print("Livros encontrados:")
                for livro in resultados:
                    status = "Disponível" if livro.disponivel else "Indisponível"
                    print(f'Título: {livro.titulo}, Autor: {livro.autor}, ISBN: {livro.isbn}, Status: {status}')
            else:
                print("Nenhum livro encontrado.")

        elif escolha == "3":
            usuario_id = input("Digite o ID do usuário: ")
            usuario = next((u for u in biblioteca.usuarios if u.id_usuario == usuario_id), None)
            if not usuario:
                print("Usuário não encontrado.")
                continue

            titulo = input("Digite o título do livro a ser emprestado: ")
            livro = next((l for l in biblioteca.livros if l.titulo == titulo), None)
            if livro:
                livro.emprestar(usuario)
            else:
                print("Livro não encontrado.")

        elif escolha == "4":
            usuario_id = input("Digite o ID do usuário: ")
            usuario = next((u for u in biblioteca.usuarios if u.id_usuario == usuario_id), None)
            if not usuario:
                print("Usuário não encontrado.")
                continue

            titulo = input("Digite o título do livro a ser devolvido: ")
            livro = next((l for l in usuario.livros_emprestados if l.titulo == titulo), None)
            if livro:
                livro.devolver(usuario)
            else:
                print("O usuário não possui esse livro.")

        elif escolha == "5":
            nome = input("Digite o nome do usuário: ")
            usuario_id = input("Digite o ID do usuário: ")
            novo_usuario = Usuario(nome, usuario_id)
            biblioteca.adicionar_usuario(novo_usuario)
            print(f'Usuário "{nome}" adicionado ao sistema.')

        elif escolha == "6":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
