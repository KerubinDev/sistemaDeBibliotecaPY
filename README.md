Projeto: Sistema de Biblioteca em Python
Descrição
Este projeto implementa um sistema simples de gerenciamento de biblioteca em Python. Ele permite a adição de livros e usuários, a busca de livros por título ou autor, o empréstimo de livros para usuários e a devolução de livros à biblioteca.

Funcionalidades
Adicionar livros à biblioteca
Adicionar usuários ao sistema
Buscar livros por título ou autor
Emprestar livros para usuários
Devolver livros à biblioteca
Estrutura do Código
O sistema é composto por quatro classes principais:

Classe Livro

Descrição: Representa um livro na biblioteca.
Atributos:
__titulo: Título do livro.
__autor: Nome do autor do livro.
__isbn: ISBN do livro.
__disponivel: Indica se o livro está disponível para empréstimo.
Métodos:
adicionar(self, biblioteca): Adiciona o livro à biblioteca.
buscar(self, termo): Busca por um termo no título ou no nome do autor.
emprestar(self, usuario): Empresta o livro para um usuário.
devolver(self, usuario): Devolve o livro à biblioteca.
Propriedades:
titulo: Retorna o título do livro.
autor: Retorna o autor do livro.
isbn: Retorna o ISBN do livro.
disponivel: Retorna se o livro está disponível ou não.
Classe Autor

Descrição: Representa um autor de livros.
Atributos:
__nome: Nome do autor.
__nacionalidade: Nacionalidade do autor.
Propriedades:
nome: Retorna o nome do autor.
nacionalidade: Retorna a nacionalidade do autor.
Classe Usuario

Descrição: Representa um usuário do sistema da biblioteca.
Atributos:
__nome: Nome do usuário.
__id_usuario: ID único do usuário.
__livros_emprestados: Lista de livros emprestados pelo usuário.
Métodos:
adicionar_livro(self, livro): Adiciona um livro à lista de livros emprestados.
remover_livro(self, livro): Remove um livro da lista de livros emprestados.
Propriedades:
nome: Retorna o nome do usuário.
id_usuario: Retorna o ID do usuário.
livros_emprestados: Retorna a lista de livros emprestados pelo usuário.
Classe Biblioteca

Descrição: Gerencia a coleção de livros e os usuários da biblioteca.
Atributos:
__livros: Lista de livros disponíveis na biblioteca.
__usuarios: Lista de usuários registrados no sistema.
Métodos:
adicionar_livro(self, livro): Adiciona um livro à biblioteca.
adicionar_usuario(self, usuario): Adiciona um usuário ao sistema.
buscar_livros(self, termo): Busca livros na biblioteca por título ou autor.
Propriedades:
livros: Retorna a lista de livros na biblioteca.
usuarios: Retorna a lista de usuários registrados no sistema.
Exemplo de Uso
python
Copiar código
biblioteca = Biblioteca()

# Criando um autor e adicionando um livro à biblioteca
autor1 = Autor("George Orwell", "Britânico")
livro1 = Livro("1984", autor1.nome, "123456789")
livro1.adicionar(biblioteca)

# Adicionando um usuário ao sistema
usuario1 = Usuario("João Silva", "001")
biblioteca.adicionar_usuario(usuario1)

# Buscando por livros na biblioteca
resultados_busca = biblioteca.buscar_livros("Orwell")
for livro in resultados_busca:
    print(f"Livro encontrado: {livro.titulo}, Autor: {livro.autor}")

# Emprestando e devolvendo um livro
livro1.emprestar(usuario1)
livro1.devolver(usuario1)
Como Executar
Clone este repositório.
Execute o script principal para testar as funcionalidades da biblioteca.
Requisitos
Python 3.x

Licença
Este projeto está licenciado sob a licença Apache-2.0 license. Consulte o arquivo LICENSE para mais detalhes.
