# Generated by Django 3.1.2 on 2021-05-09 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20210509_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listes',
            name='sujet',
            field=models.CharField(choices=[('Positf', 'positif'), ('Négatif', 'cas contact'), ('Syptomatique', 'symptomatique'), ('Autres', 'autres')], default='Positf', max_length=255),
        ),
    ]
