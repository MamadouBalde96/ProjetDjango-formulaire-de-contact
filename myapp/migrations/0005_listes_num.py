# Generated by Django 3.1.2 on 2021-05-09 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210509_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='listes',
            name='num',
            field=models.CharField(choices=[('01', 'étudiant'), ('02', 'enseignant'), ('03', 'apprenant en formation continue')], default='01', max_length=2),
        ),
    ]
