# Generated by Django 3.1.2 on 2020-11-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0007_auto_20201107_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement des infos"),
        ),
    ]
