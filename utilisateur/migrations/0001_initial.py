# Generated by Django 3.1.2 on 2020-11-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(help_text='Enter field documentation', max_length=20, verbose_name='Nom')),
                ('prenom', models.CharField(help_text='Enter field documentation', max_length=20, verbose_name='Prénom')),
                ('dateNaissance', models.DateField(help_text='Enter field documentation', max_length=20, verbose_name='Date de naissance')),
                ('email', models.CharField(help_text='Enter field documentation', max_length=20, verbose_name='E-mail')),
                ('telephone', models.CharField(help_text='Enter field documentation', max_length=20, verbose_name='Téléphone')),
                ('telephoneSupplementaire', models.CharField(blank=True, help_text='Enter field documentation', max_length=20, null=True, verbose_name='Autre Téléphone supplémentaire')),
                ('condition', models.BooleanField(help_text='Enter field documentation', verbose_name="Condition d'utilisation")),
                ('nombreSiegeReserve', models.IntegerField(default=1, help_text='Enter field documentation', verbose_name='Nombre de place à réserver')),
                ('nombreEnfants', models.IntegerField(default=0, help_text='Enter field documentation', verbose_name="Nombre d'enfant")),
                ('recevoirAlert', models.BooleanField(default=False, help_text='Enter field documentation', verbose_name='Reception des alertes')),
            ],
        ),
    ]
