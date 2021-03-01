# Generated by Django 3.1.7 on 2021-02-27 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agence', '0007_reponse'),
        ('banques', '0002_interîlesair'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateVente', models.DateTimeField(auto_now_add=True, verbose_name="Date d'achat")),
                ('montantDeVente', models.IntegerField(verbose_name="Montant de l'achat")),
                ('reduction', models.IntegerField(verbose_name="Montant redut sur le montant de l'achat")),
                ('agence', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='agence.agence', verbose_name='Agence')),
            ],
            options={
                'verbose_name': 'Banque principal',
            },
        ),
        migrations.CreateModel(
            name='StatistiqueVente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateVente', models.DateTimeField(auto_now_add=True, verbose_name="Date d'achat")),
                ('montantDeVente', models.IntegerField(verbose_name="Montant de l'achat")),
                ('agence', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='agence.agence', verbose_name='Agence')),
            ],
            options={
                'verbose_name': 'Statistiques des vente',
            },
        ),
        migrations.RemoveField(
            model_name='banqueagenceprincipal',
            name='agence',
        ),
        migrations.DeleteModel(
            name='Gombessa',
        ),
        migrations.DeleteModel(
            name='InterÎlesAir',
        ),
        migrations.DeleteModel(
            name='BanqueAgencePrincipal',
        ),
    ]