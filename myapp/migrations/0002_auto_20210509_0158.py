# Generated by Django 3.1.2 on 2021-05-08 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listes',
            name='promotion',
            field=models.CharField(blank=True, choices=[('1', 'L1'), ('2', 'L2'), ('3', 'L3'), ('4', 'M1'), ('5', 'M2')], default='1', help_text='chosir votre niveau', max_length=1),
        ),
        migrations.AlterField(
            model_name='listes',
            name='TestCovid',
            field=models.FileField(upload_to='pdf'),
        ),
        migrations.AlterField(
            model_name='listes',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
