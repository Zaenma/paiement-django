# Generated by Django 3.1.2 on 2020-11-05 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0002_auto_20201105_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='titre',
            field=models.CharField(choices=[('Monsieur', 'Monsieur'), ('Madame', 'Madame')], max_length=30, verbose_name='Titre'),
        ),
    ]