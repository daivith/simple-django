# Generated by Django 3.1 on 2020-08-24 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(max_length=100, verbose_name='Sobrenome'),
        ),
    ]
