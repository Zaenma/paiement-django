# Generated by Django 3.1.2 on 2020-11-06 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voyage_prevu', '0036_auto_20201106_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aeroport',
            old_name='non',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='port',
            old_name='non',
            new_name='nom',
        ),
    ]
