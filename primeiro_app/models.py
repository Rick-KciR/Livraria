from django.db import models


class Autor(models.Model):
    nome = models.CharField("Nome Completo", max_length=200)
    email = models.EmailField("Email", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField("Categoria", max_length=200)
    descricao = models.TextField("Descrição")

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField("Título", max_length=200)
    autor = models.ManyToManyField(Autor)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria", blank=True, null=True)
    data_publicacao = models.DateField(blank=True, null=True)
    edicao = models.CharField("Edição", max_length=200, blank=True, null=True)
    genero = models.CharField("Gênero textual", max_length=200, blank=True, null=True)
    editora = models.CharField("Editora", max_length=200, blank=True, null=True)
    valor = models.DecimalField("Valor", max_digits=7, decimal_places=2,  default=99.99)
    #imagem = models.ImageField(upload_to='livraria/media', blank=True)
    descricao = models.TextField(blank=True, null=True)
    isbn = models.CharField("ISBN", max_length=13, unique=True, help_text="13 Caracteres <a "
                                                                          "href='https://www.isbn-international.org/content/what-isbn""'>ISBN number</a>")


    class Meta:
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.titulo
        if len(self.descricao > 50):
            return self.descricao[:50] + "..."


class Cliente(models.Model):
    nome = models.CharField("Nome Completo", max_length=200)
    cpf = models.CharField("Cpf", max_length=11)
    email = models.EmailField("Email", blank=True, null=True)
    celular = models.CharField("Celular", max_length=14)

    class Meta:
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    cliente = models.ManyToManyField(Cliente)
    rua = models.CharField("Rua/Avenida", max_length=200)
    numero = models.CharField("Número", max_length=5)
    bairro = models.CharField("Bairro", max_length=200)
    cidade = models.CharField("Cidade", max_length=200)
    estado = models.CharField("Estado", max_length=200)

    class Meta:
        verbose_name_plural = "Endereços"

    def __str__(self):
        return self.cliente

