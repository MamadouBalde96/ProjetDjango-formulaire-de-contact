# Generated by Django 3.1.2 on 2021-05-15 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20210515_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listes',
            name='parcours',
            field=models.CharField(choices=[('MIAGE', 'MIAGE'), ('MATHS', 'MATHS'), ('ECONOMIE', 'ECONOMIE'), ('GESTION', 'GESTION'), ('DOUBLE LICENCE', 'DOUBLE LICENCE'), ('AUTRES PARCOURS', 'AUTRES PARCOURS')], default='MIAGE', max_length=255),
        ),
    ]
