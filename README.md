# 🏛️ Sistema de Biblioteca em Python

## 📚 Descrição do Projeto

O **Sistema de Biblioteca em Python** é uma aplicação que simula as operações básicas de uma biblioteca tradicional. Ele permite o gerenciamento de livros, autores e usuários, possibilitando funções como adicionar livros à biblioteca, buscar títulos, emprestar e devolver exemplares, além de gerenciar os usuários cadastrados.

Este projeto foi concebido como uma forma de explorar conceitos fundamentais de POO (Programação Orientada a Objetos) em Python, estruturando um sistema modular e escalável.

---

## 🛠️ Funcionalidades Principais

- **Gestão de Livros**: Adicionar novos livros à biblioteca, buscar por títulos ou autores, e controlar o status de disponibilidade dos livros.
- **Gestão de Usuários**: Cadastro de novos usuários, gerenciamento de livros emprestados, e acompanhamento do histórico de empréstimos.
- **Empréstimo e Devolução**: Emprestar livros para usuários e registrar a devolução, garantindo a integridade do sistema e o controle de disponibilidade.

---

## ⚙️ Estrutura do Código

O sistema é dividido em quatro classes principais:

### 1. Classe `Livro`

#### 📋 Descrição:
A classe `Livro` representa um livro na biblioteca, encapsulando informações como título, autor, ISBN e status de disponibilidade.

#### 📦 Atributos:
- `__titulo` (str): O título do livro.
- `__autor` (str): O nome do autor do livro.
- `__isbn` (str): O número ISBN do livro.
- `__disponivel` (bool): Indica se o livro está disponível para empréstimo.

#### 🔧 Métodos:
- `adicionar(self, biblioteca)`: Adiciona o livro à biblioteca especificada.
- `buscar(self, termo)`: Verifica se o termo fornecido corresponde ao título ou autor do livro.
- `emprestar(self, usuario)`: Empresta o livro para um usuário, caso esteja disponível.
- `devolver(self, usuario)`: Devolve o livro emprestado, tornando-o disponível novamente.

#### 🧾 Propriedades:
- `titulo`: Retorna o título do livro.
- `autor`: Retorna o nome do autor.
- `isbn`: Retorna o ISBN do livro.
- `disponivel`: Retorna o status de disponibilidade do livro.

### 2. Classe `Autor`

#### 📋 Descrição:
A classe `Autor` representa um autor, com nome e nacionalidade, e pode ser associada a um ou mais livros.

#### 📦 Atributos:
- `__nome` (str): O nome do autor.
- `__nacionalidade` (str): A nacionalidade do autor.

#### 🧾 Propriedades:
- `nome`: Retorna o nome do autor.
- `nacionalidade`: Retorna a nacionalidade do autor.

### 3. Classe `Usuario`

#### 📋 Descrição:
A classe `Usuario` representa um usuário do sistema da biblioteca, responsável por emprestar e devolver livros.

#### 📦 Atributos:
- `__nome` (str): O nome do usuário.
- `__id_usuario` (str): O identificador único do usuário.
- `__livros_emprestados` (list): A lista de livros atualmente emprestados pelo usuário.

#### 🔧 Métodos:
- `adicionar_livro(self, livro)`: Adiciona um livro à lista de livros emprestados pelo usuário.
- `remover_livro(self, livro)`: Remove um livro da lista de livros emprestados pelo usuário.

#### 🧾 Propriedades:
- `nome`: Retorna o nome do usuário.
- `id_usuario`: Retorna o ID do usuário.
- `livros_emprestados`: Retorna a lista de livros emprestados pelo usuário.

### 4. Classe `Biblioteca`

#### 📋 Descrição:
A classe `Biblioteca` gerencia a coleção de livros e usuários, além de oferecer funcionalidades para buscar livros e registrar empréstimos e devoluções.

#### 📦 Atributos:
- `__livros` (list): Lista de livros disponíveis na biblioteca.
- `__usuarios` (list): Lista de usuários registrados na biblioteca.

#### 🔧 Métodos:
- `adicionar_livro(self, livro)`: Adiciona um livro à biblioteca.
- `adicionar_usuario(self, usuario)`: Adiciona um usuário ao sistema.
- `buscar_livros(self, termo)`: Busca livros na biblioteca com base em um termo (título ou autor).

#### 🧾 Propriedades:
- `livros`: Retorna a lista de livros na biblioteca.
- `usuarios`: Retorna a lista de usuários cadastrados na biblioteca.

---

## 📝 Exemplo de Uso

Aqui está um exemplo de como você pode utilizar as funcionalidades do sistema de biblioteca:

```python
# Criação de uma instância da biblioteca
biblioteca = Biblioteca()

# Adicionando um autor e um livro à biblioteca
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

# Emprestando um livro ao usuário
livro1.emprestar(usuario1)

# Devolvendo o livro à biblioteca
livro1.devolver(usuario1)
```

---

## 🧑‍💻 Boas Práticas e Considerações

### Organização do Código
- **Modularidade**: Cada classe é responsável por uma entidade única (Livro, Autor, Usuário, Biblioteca), mantendo o código limpo e organizado.
- **Encapsulamento**: Os atributos das classes são privados, acessíveis apenas por métodos e propriedades públicas, garantindo a integridade dos dados.

### Manutenibilidade
- **Escalabilidade**: A arquitetura do sistema permite a fácil adição de novas funcionalidades sem comprometer as existentes.
- **Testabilidade**: As classes e métodos são projetados de forma que possam ser facilmente testados individualmente.

### Segurança
- **Controle de Acesso**: Métodos e atributos privados garantem que os dados não sejam manipulados indevidamente de fora das classes.

---

## 🚀 Como Executar

1. Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com/usuario/sistema-biblioteca-python.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd sistema-biblioteca-python
   ```

3. Execute o script principal para testar as funcionalidades da biblioteca:
   ```bash
   python main.py
   ```

---

## 🧩 Contribuições

Contribuições são extremamente bem-vindas! Se você tem uma ideia para melhorar o sistema, corrija um bug ou adicione uma nova funcionalidade, siga os passos abaixo:

1. **Fork** este repositório.
2. Crie uma **branch** com a nova funcionalidade:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Faça o **commit** das suas alterações:
   ```bash
   git commit -m 'Adiciona nova funcionalidade X'
   ```
4. Envie as alterações para a sua branch:
   ```bash
   git push origin feature/nova-funcionalidade
   ```
5. Abra um **Pull Request** detalhando as alterações realizadas.

---

## 📝 Licença

Este projeto está licenciado sob a licença Apache-2.0 license. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📖 Glossário

- **ISBN**: International Standard Book Number, um identificador único para livros.
- **POO**: Programação Orientada a Objetos, um paradigma de programação baseado no conceito de "objetos", que podem conter dados e métodos.
- **Encapsulamento**: O conceito de esconder os detalhes internos de um objeto e expor apenas o que é necessário.

---

## 🛠️ Requisitos do Sistema

- **Python 3.x**: Certifique-se de que você tenha uma versão compatível do Python instalada em seu sistema.

---

## 🧠 Referências

- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [GitHub Docs](https://docs.github.com/)

---

## 📬 Contato

Caso tenha dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

- **Nome**: Kelvin Moraes(kerubin)
- **Email**: kelvin.moraes117@gmail.com

---
