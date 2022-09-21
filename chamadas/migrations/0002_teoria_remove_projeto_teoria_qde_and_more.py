# Generated by Django 4.0.6 on 2022-09-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamadas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teoria_total', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=6)),
                ('teoria_qde', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='teoria_qde',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='teoria_total',
        ),
    ]
