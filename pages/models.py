from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    texto = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    imagem = models.ImageField(upload_to='img/', max_length=100)
