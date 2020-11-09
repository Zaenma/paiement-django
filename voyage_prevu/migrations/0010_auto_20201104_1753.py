# Generated by Django 3.1.2 on 2020-11-04 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage_prevu', '0009_auto_20201104_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='voyagesprevu',
            name='bagage',
            field=models.IntegerField(null=True, verbose_name='Quantité de bagage autorisé'),
        ),
        migrations.AlterField(
            model_name='voyagesprevu',
            name='datearrivee',
            field=models.DateTimeField(null=True, verbose_name="Date d'arrivée à prevoir"),
        ),
        migrations.AlterField(
            model_name='voyagesprevu',
            name='villeEscale',
            field=models.ManyToManyField(null=True, related_name='Ville_escale', to='voyage_prevu.Ville', verbose_name="Villes d'sscale (si l'on prevoit)"),
        ),
    ]
