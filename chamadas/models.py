from datetime import date
from django.db import models
from users.models import Profile

# Create your models here.

class ProjetoModelo(models.Model):
    nome = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    bibliografia_total = models.IntegerField(default=10, blank=True)
    introducao_titulo_1 = models.CharField(
        max_length=100,
        default='Qual é o significado?',
        verbose_name = '1. Introdução (parâmetro): Título'
        )
    introducao_peso_1 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.2,
        verbose_name='2. Introdução (parâmetro): Peso'
        )
    introducao_titulo_2 = models.CharField(
        max_length=100,
        default='Qual é a utilidade?',
        verbose_name = '2. Introdução (parâmetro): Título'
        )
    introducao_peso_2 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.2,
        verbose_name='1. Introdução (parâmetro): Peso'
        )
    introducao_titulo_3 = models.CharField(
        max_length=100,
        default='Quais as vantagens e desvantagens?',
        verbose_name = '3. Introdução (parâmetro): Título'
        )
    introducao_peso_3 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.2,
        verbose_name='3. Introdução (parâmetro): Peso'
        )
    introducao_titulo_4 = models.CharField(
        max_length=100,
        default='O que já foi feito sobre o assunto?',
        verbose_name = '4. Introdução (parâmetro): Título'
        )
    introducao_peso_4 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.2,
        verbose_name='4. Introdução (parâmetro): Peso'
        )
    introducao_titulo_5 = models.CharField(
        max_length=100,
        default='As referências bibliográficas foram citadas corretamente?',
        verbose_name = '5. Introdução (parâmetro): Título'
        )
    introducao_peso_5 = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0.2,
        verbose_name='5. Introdução (parâmetro): Peso'
        )

    introducao_peso = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=0,
        verbose_name='Introdução: Peso'
        )

    def __str__(self):
        return self.nome

class Chamada(models.Model):
    nome = models.CharField(max_length=7, unique=True)
    projetomodelo = models.ForeignKey(ProjetoModelo, on_delete=models.PROTECT, null=True)
    deadline_inscricao = models.DateField(verbose_name='Data limite da inscrição', null=True)
    deadline_bibliografia = models.DateField(verbose_name='Data limite da bibliografia', null=True)
    deadline_proposta = models.DateField(verbose_name='Data limite da proposta', null=True)
    deadline_projeto = models.DateField(verbose_name='Data limite do projeto', null=True)
    deadline_chamada = models.DateField(verbose_name='Data limite da chamada', null=True)
    resumo = models.TextField()
    edital = models.FileField(upload_to='pdf/%Y/%m/%d/')
    aviso = models.TextField(null=True, blank=True)

    def get_status(self):
        if date.today() > self.deadline_inscricao:
            if date.today() > self.deadline_chamada:
                data = "Encerrado"
            else:
                data = "Em andamento"
        else:
            data = "Aberto"
        return data

    def get_bibliografia(self):
        if date.today() > self.deadline_bibliografia:
            return False
        else:
            return True

    def get_proposta(self):
        if date.today() > self.deadline_proposta:
            return False
        else:
            return True

    def get_projeto(self):
        if date.today() > self.deadline_projeto:
            return False
        else:
            return True

    def __str__(self):
        return self.nome

class Tema(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    requisitos = models.TextField()

    def __str__(self):
        return self.titulo

class Inscricao(models.Model):
    created = models.DateField(auto_now_add=True)
    tema = models.ForeignKey(Tema, on_delete=models.PROTECT)
    lider = models.ForeignKey(Profile, on_delete=models.CASCADE)
    chamada = models.ForeignKey(Chamada, on_delete=models.CASCADE)
    equipe = models.CharField(max_length=100)
    membro_1 = models.CharField(max_length=100, null=True, blank=True)
    membro_2 = models.CharField(max_length=100, null=True, blank=True)
    membro_3 = models.CharField(max_length=100, null=True, blank=True)
    ranking = models.IntegerField(null=True)

    def __str__(self):
        return self.equipe

class Extra(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    penalidade = models.DecimalField(max_digits=6, decimal_places=3, default=0, blank=True)
    divulgacao = models.DecimalField(max_digits=6, decimal_places=3, default=0, blank=True)
    nota = models.DecimalField(max_digits=6, decimal_places=3, default=0, blank=True)

    def setNota(self):
        self.nota = self.penalidade+self.divulgacao
        return self.nota

class Projeto(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    inscricao = models.OneToOneField(Inscricao, on_delete=models.CASCADE)
    modelo = models.ForeignKey(ProjetoModelo, on_delete=models.PROTECT)

    titulo = models.CharField(max_length=100, null=True, blank=True)
    nota = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    arquivo = models.FileField(upload_to='pdf/%Y/%m/%d/', null=True)

    def setNota(self):
        data = self.introducao.nota_introducao
        return data

    def __str__(self):
        return self.titulo

class Introducao(models.Model):

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE)

    introducao_nota_1 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0, blank=True)
    introducao_nota_2 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0, blank=True)
    introducao_nota_3 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0, blank=True)
    introducao_nota_4 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0, blank=True)
    introducao_nota_5 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0, blank=True)
    introducao_consideracao_1 = models.CharField(max_length=255, null=True, blank=True)
    introducao_consideracao_2 = models.CharField(max_length=255, null=True, blank=True)
    introducao_consideracao_3 = models.CharField(max_length=255, null=True, blank=True)
    introducao_consideracao_4 = models.CharField(max_length=255, null=True, blank=True)
    introducao_consideracao_5 = models.CharField(max_length=255, null=True, blank=True)

    nota_introducao = models.DecimalField(max_digits=6, decimal_places=3, default=0.0, blank=True)

    def setNotaIntroducao(self):
        data = self.projeto.modelo.introducao_peso_1*self.introducao_nota_1
        data += self.projeto.modelo.introducao_peso_2*self.introducao_nota_2
        data += self.projeto.modelo.introducao_peso_3*self.introducao_nota_3
        data += self.projeto.modelo.introducao_peso_4*self.introducao_nota_4
        data += self.projeto.modelo.introducao_peso_5*self.introducao_nota_5
        data = data*self.projeto.modelo.introducao_peso
        return data

class Teoria(models.Model):

    teoria_total = models.DecimalField(max_digits=6, decimal_places=3, default=0, blank=True)
    teoria_qde = models.DecimalField(max_digits=6, decimal_places=3, default=0, blank=True)
    nota_teoria = models.DecimalField(max_digits=6, decimal_places=3, default=0.0, blank=True)

    def setNotaTeoria(self):
        data = self.teoria_qte*100.0/self.teoria_total
        return data