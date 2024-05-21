# Generated by Django 5.0.6 on 2024-05-21 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_networknode_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(max_length=255, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='network_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='network.networknode', verbose_name='Узел сети'),
        ),
        migrations.AlterField(
            model_name='product',
            name='release_date',
            field=models.DateField(verbose_name='Дата выхода'),
        ),
    ]