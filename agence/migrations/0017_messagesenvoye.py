# Generated by Django 3.1.7 on 2021-03-15 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agence', '0016_auto_20210314_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessagesEnvoye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('sujet', models.CharField(max_length=255, verbose_name='Titre du message')),
                ('message', models.TextField(verbose_name='Messages')),
                ('dateEnvoie', models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoie")),
            ],
            options={
                'verbose_name': 'Messages envoyé',
            },
        ),
    ]