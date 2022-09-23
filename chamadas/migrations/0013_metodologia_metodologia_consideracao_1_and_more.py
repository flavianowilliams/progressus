# Generated by Django 4.0.6 on 2022-09-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamadas', '0012_alter_projetomodelo_resultado_peso_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='metodologia',
            name='metodologia_consideracao_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metodologia',
            name='metodologia_consideracao_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metodologia',
            name='metodologia_consideracao_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metodologia',
            name='metodologia_consideracao_4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metodologia',
            name='metodologia_consideracao_5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metodologia',
            name='metodologia_nota_1',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='metodologia',
            name='metodologia_nota_2',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='metodologia',
            name='metodologia_nota_3',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='metodologia',
            name='metodologia_nota_4',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='metodologia',
            name='metodologia_nota_5',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='projetomodelo',
            name='metodologia_peso_1',
            field=models.DecimalField(decimal_places=3, default=0.02, max_digits=6, verbose_name='2. Introdução (parâmetro): Peso'),
        ),
        migrations.AddField(
            model_name='projetomodelo',
            name='metodologia_peso_2',
            field=models.DecimalField(decimal_places=3, default=0.02, max_digits=6, verbose_name='1. Introdução (parâmetro): Peso'),
        ),
        migrations.AddField(
            model_name='projetomodelo',
            name='metodologia_peso_3',
            field=models.DecimalField(decimal_places=3, default=0.02, max_digits=6, verbose_name='3. Introdução (parâmetro): Peso'),
        ),
        migrations.AddField(
            model_name='projetomodelo',
            name='metodologia_peso_4',
            field=models.DecimalField(decimal_places=3, default=0.02, max_digits=6, verbose_name='4. Introdução (parâmetro): Peso'),
        ),
        migrations.AddField(
            model_name='projetomodelo',
            name='metodologia_peso_5',
            field=models.DecimalField(decimal_places=3, default=0.02, max_digits=6, verbose_name='5. Introdução (parâmetro): Peso'),
        ),
        migrations.AddField(
            model_name='projetomodelo',
            name='metodologia_titulo_1',
            field=models.CharField(default='Como o equipamento ou experimento poderia ser reproduzido?', max_length=100, verbose_name='1. Introdução (parâmetro): Título'),
        ),
        migrations.AddField(
            model_name='projetomodelo',
            name='metodologia_titulo_2',
            field=models.CharField(default='A lista de materiais e/ou softwares necessários foi fornecido?', max_length=100, verbose_name='2. Introdução (parâmetro): Título'),
        ),
        migrations.AddField(
            model_name='projetomodelo',
            name='metodologia_titulo_3',
            field=models.CharField(default='O custo financeiro total ou detalhado por item foi fornecido?', max_length=100, verbose_name='3. Introdução (parâmetro): Título'),
        ),
        migrations.AddField(
            model_name='projetomodelo',
            name='metodologia_titulo_4',
            field=models.CharField(default='O procedimento para a perfeita utilização foi apresentado de maneira clara e objetiva?', max_length=100, verbose_name='4. Introdução (parâmetro): Título'),
        ),
        migrations.AddField(
            model_name='projetomodelo',
            name='metodologia_titulo_5',
            field=models.CharField(default='Uma imagem clara do dispositivo, ou no caso de software o link para o seu repositório foi fornecido?', max_length=100, verbose_name='5. Introdução (parâmetro): Título'),
        ),
        migrations.AlterField(
            model_name='metodologia',
            name='nota_metodologia',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=7),
        ),
    ]
