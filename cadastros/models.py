from chamadas.models import Chamada, ProjetoModelo, Tema, Turma
from users.models import Profile
from pages.models import Noticia
from django.db import models

# Create your models here.

class CadastroProfile(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.profile

class CadastroChamada(models.Model):
    chamada = models.OneToOneField(Chamada, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.chamada.nome

class CadastroNoticia(models.Model):
    noticia = models.OneToOneField(Noticia, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.noticia.titulo

class CadastroTema(models.Model):
    tema = models.OneToOneField(Tema, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.tema.titulo

class CadastroProjeto(models.Model):
    projeto = models.OneToOneField(ProjetoModelo, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.projeto.nome

class CadastroTurma(models.Model):
    turma = models.OneToOneField(Turma, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.turma.nome
