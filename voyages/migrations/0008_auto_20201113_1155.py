# Generated by Django 3.1.2 on 2020-11-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyages', '0007_auto_20201113_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyagesparbateau',
            name='dateArrivee',
            field=models.DateTimeField(null=True, verbose_name="Date d'arrivée à prevoir"),
        ),
    ]