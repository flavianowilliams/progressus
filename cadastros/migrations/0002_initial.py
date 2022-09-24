# Generated by Django 4.0.6 on 2022-09-23 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chamadas', '0001_initial'),
        ('users', '0002_alter_profile_turma'),
        ('cadastros', '0001_initial'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrotema',
            name='tema',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chamadas.tema'),
        ),
        migrations.AddField(
            model_name='cadastroprojeto',
            name='projeto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chamadas.projetomodelo'),
        ),
        migrations.AddField(
            model_name='cadastroprofile',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='cadastronoticia',
            name='noticia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.noticia'),
        ),
        migrations.AddField(
            model_name='cadastrochamada',
            name='chamada',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chamadas.chamada'),
        ),
    ]
