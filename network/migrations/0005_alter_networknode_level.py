# Generated by Django 5.0.6 on 2024-05-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_networknode_options_networknode_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networknode',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Factory'), (1, 'Retail Network'), (2, 'Individual Entrepreneur')], editable=False),
        ),
    ]
