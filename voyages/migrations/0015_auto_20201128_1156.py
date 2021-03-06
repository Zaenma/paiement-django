# Generated by Django 3.1.2 on 2020-11-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyages', '0014_auto_20201128_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyagesparavion',
            name='dateAjoutee',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date d'integration "),
        ),
        migrations.AlterField(
            model_name='voyagesparavion',
            name='dateModifiee',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification '),
        ),
        migrations.AlterField(
            model_name='voyagesparbateau',
            name='dateAjoutee',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date d'integration "),
        ),
        migrations.AlterField(
            model_name='voyagesparbateau',
            name='dateModifiee',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification '),
        ),
        migrations.AlterField(
            model_name='voyagesparbu',
            name='dateAjoutee',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date d'integration "),
        ),
        migrations.AlterField(
            model_name='voyagesparbu',
            name='dateModifiee',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification '),
        ),
    ]
