# Generated by Django 4.1.6 on 2023-03-05 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamadas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bibliografia',
            name='arquivo',
            field=models.FileField(default='modelo-vazio.pdf', null=True, upload_to='pdf/%Y/%m/%d/'),
        ),
    ]
