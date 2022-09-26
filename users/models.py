from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=50, null=True)
    turma = models.CharField(max_length=4, null=True)
    profile_status = models.CharField(
        max_length=10,
        default="Adimplente",
        choices=(("adimplente", "Adimplente"), ("em_debito", "Em débito"))
        )

    def __str__(self):
        return self.nome_completo