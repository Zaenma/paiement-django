# Generated by Django 3.1.2 on 2020-11-03 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agence', '0001_initial'),
        ('voyage_prevu', '0005_auto_20201103_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyagesprevu',
            name='agencePrincipal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='agence.agence', verbose_name='Agence Organisatrice du voyage'),
        ),
    ]
