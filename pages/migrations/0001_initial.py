# Generated by Django 4.0.6 on 2022-09-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True)),
                ('texto', models.TextField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('imagem', models.ImageField(upload_to='img/')),
            ],
        ),
    ]
