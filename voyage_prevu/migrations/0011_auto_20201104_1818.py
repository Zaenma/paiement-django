# Generated by Django 3.1.2 on 2020-11-04 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voyage_prevu', '0010_auto_20201104_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voyagesprevu',
            name='villeEscale',
        ),
        migrations.AddField(
            model_name='voyagesprevu',
            name='villeEscale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='Ville_escale', to='voyage_prevu.ville', verbose_name="Villes d'sscale (si l'on prevoit)"),
        ),
    ]
