from users.models import Profile
from django.db import models

# Create your models here.

class CadastroProfile(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
