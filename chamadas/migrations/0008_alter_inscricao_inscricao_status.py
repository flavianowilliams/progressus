# Generated by Django 4.1.6 on 2023-05-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamadas', '0007_alter_inscricao_inscricao_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='inscricao_status',
            field=models.CharField(choices=[('comum', 'Comum'), ('destaque', 'Em destaque')], default='comum', max_length=12),
        ),
    ]