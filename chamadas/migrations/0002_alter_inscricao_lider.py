# Generated by Django 4.0.6 on 2022-09-18 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_turma'),
        ('chamadas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='lider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
