# Generated by Django 3.1.2 on 2020-11-28 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voyages', '0013_auto_20201128_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voyagesparavion',
            old_name='dateAjout',
            new_name='dateAjoutee',
        ),
        migrations.RenameField(
            model_name='voyagesparbateau',
            old_name='dateAjout',
            new_name='dateAjoutee',
        ),
        migrations.RenameField(
            model_name='voyagesparbu',
            old_name='dateAjout',
            new_name='dateAjoutee',
        ),
    ]