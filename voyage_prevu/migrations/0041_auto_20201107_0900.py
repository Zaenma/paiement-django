# Generated by Django 3.1.2 on 2020-11-07 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voyage_prevu', '0040_auto_20201107_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aeroport',
            name='ile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage_prevu.ile', verbose_name='Cette ville se situe sur quelle île ?'),
        ),
        migrations.AlterField(
            model_name='aeroport',
            name='nom',
            field=models.CharField(max_length=50, verbose_name='Les villes où se situent les aéroport'),
        ),
        migrations.AlterField(
            model_name='port',
            name='ile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage_prevu.ile', verbose_name='Cette ville se situe sur quelle île ?'),
        ),
        migrations.AlterField(
            model_name='port',
            name='nom',
            field=models.CharField(max_length=50, verbose_name='Les villes où se situent les ports'),
        ),
    ]
