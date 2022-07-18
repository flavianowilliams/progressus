from users.models import Profile
from django.db import models

# Create your models here.

class CadastroProfile(Profile):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)