# Generated by Django 3.1.7 on 2021-03-02 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agence', '0009_auto_20210301_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agence',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
