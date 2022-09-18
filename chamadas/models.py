from datetime import date
from django.db import models
from users.models import Profile

# Create your models here.

class Chamada(models.Model):
    nome = models.CharField(max_length=7, unique=True)
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

class Projeto(models.Model):
    nota = models.DecimalField(max_digits=6, decimal_places=3, default=0, blank=True)

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
