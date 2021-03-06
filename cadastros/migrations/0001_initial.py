# Generated by Django 4.0.6 on 2022-07-18 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_profile_turma'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
