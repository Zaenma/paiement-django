# Generated by Django 3.1.7 on 2021-03-05 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0012_abonnemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbonnesHebdomadaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(help_text='Nom du client', max_length=20, verbose_name='Nom')),
                ('prenom', models.CharField(help_text='Prenom du client', max_length=20, verbose_name='Prénom')),
                ('codeAbonnement', models.CharField(help_text="Code d'abonnement", max_length=20, unique=True, verbose_name="Code d'abonnement")),
                ('dateNaissance', models.DateField(help_text='Date de nissance', max_length=20, verbose_name='Date de naissance')),
                ('email', models.CharField(help_text='Adresse e-mail', max_length=100, verbose_name='E-mail')),
                ('telephone', models.CharField(help_text='Téléphone principale', max_length=20, verbose_name='Téléphone')),
                ('nombreVoyageParMois', models.IntegerField(blank=True, help_text='Nombre de voyags', null=True, verbose_name='Nombre de voyages par mois')),
                ('dateAbonnement', models.DateTimeField(auto_now_add=True, verbose_name="Date d'abonnement")),
                ('montantMensuelVerse', models.IntegerField(help_text='Montant par mois', verbose_name='Montant minimum à verser par mois')),
            ],
            options={
                'verbose_name': 'Abonnements Hebdomadaire',
            },
        ),
    ]
