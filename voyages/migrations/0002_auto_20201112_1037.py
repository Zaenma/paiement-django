# Generated by Django 3.1.2 on 2020-11-12 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voyagesparavion',
            old_name='datearrivee',
            new_name='dateArrivee',
        ),
        migrations.RenameField(
            model_name='voyagesparbateau',
            old_name='datearrivee',
            new_name='dateArrivee',
        ),
        migrations.RenameField(
            model_name='voyagesparbu',
            old_name='datearrivee',
            new_name='dateArrivee',
        ),
        migrations.RemoveField(
            model_name='voyagesparavion',
            name='dateretour',
        ),
        migrations.RemoveField(
            model_name='voyagesparbateau',
            name='dateretour',
        ),
        migrations.RemoveField(
            model_name='voyagesparbu',
            name='dateretour',
        ),
        migrations.AddField(
            model_name='voyagesparavion',
            name='dateRetour',
            field=models.DateTimeField(blank=True, null=True, verbose_name="Date d'arrivée à prevoir"),
        ),
        migrations.AddField(
            model_name='voyagesparbateau',
            name='dateRetour',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date de retour'),
        ),
        migrations.AddField(
            model_name='voyagesparbu',
            name='dateRetour',
            field=models.DateTimeField(blank=True, null=True, verbose_name="Date d'arrivée à prevoir"),
        ),
    ]
