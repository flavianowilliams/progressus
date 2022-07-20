from datetime import date
from django.db import models

# Create your models here.

class Chamada(models.Model):
    nome = models.CharField(max_length=7, unique=True)
    deadline_inscricao = models.DateField(verbose_name='Data limite da inscrição', null=True)
    deadline_bibliografia = models.DateField(verbose_name='Data limite da bibliografia', null=True)
    deadline_proposta = models.DateField(verbose_name='Data limite da proposta', null=True)
    deadline_projeto = models.DateField(verbose_name='Data limite do projeto', null=True)
    deadline_chamada = models.DateField(verbose_name='Data limite da chamada', null=True)
    resumo = models.TextField()
    edital = models.FileField()
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

    def __str__(self):
        return self.nome

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
