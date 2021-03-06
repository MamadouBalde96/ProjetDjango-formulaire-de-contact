# Generated by Django 3.1.2 on 2021-05-14 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20210511_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='listes',
            name='UFR',
            field=models.CharField(choices=[('Sciences Economiques, Gestion, Mathématiques, Informatique (SEGMI)', 'Sciences Economiques, Gestion, Mathématiques, Informatique (SEGMI)'), ('Langues et Cultures Etrangères (LCE)', 'Langues et Cultures Etrangères (LCE)'), ('Philosophie, Information-Communication, Langage, Littérature, Arts du spectacle (PHILLIA)', 'Philosophie, Information-Communication, Langage, Littérature, Arts du spectacle (PHILLIA)'), ('Droit et Science Politique (DSP)', 'Droit et Science Politique (DSP)'), ("Sciences Psychologiques et Sciences de l'Education (SPSE)", "Sciences Psychologiques et Sciences de l'Education (SPSE)"), ('Sciences Sociales et Administration (SSA)', 'Sciences Sociales et Administration (SSA)'), ('Sciences et Techniques des Activités Physiques et Sportives (STAPS)', 'Sciences et Techniques des Activités Physiques et Sportives (STAPS)'), ("IUT Ville d'Avray/St Cloud/Nanterre", 'Systèmes Industriels et Techniques de Communication (SITEC)'), ("IUT Ville d'Avray/St Cloud/Nanterre", "IUT Ville d'Avray/St Cloud/Nanterre")], default='Sciences Economiques, Gestion, Mathématiques, Informatique (SEGMI)', max_length=255),
        ),
        migrations.AlterField(
            model_name='listes',
            name='sujet',
            field=models.CharField(choices=[('Positif', 'Positif'), ('Cas contact', 'Cas contact'), ('Syptomatique', 'Symptomatique'), ('Autres', 'Autres')], default='Positif', max_length=255),
        ),
    ]
