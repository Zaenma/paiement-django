# Generated by Django 3.1.7 on 2021-03-04 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agence', '0014_auto_20210301_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agence',
            name='responsable',
            field=models.CharField(max_length=50, unique=True, verbose_name="Responsable de l'agence"),
        ),
    ]
