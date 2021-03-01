# Generated by Django 3.1.2 on 2020-11-28 11:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('voyages', '0012_auto_20201124_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='voyagesparavion',
            name='dateAjout',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 11, 28, 11, 28, 28, 271776, tzinfo=utc), verbose_name="Date d'integration"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voyagesparavion',
            name='dateModifiee',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AddField(
            model_name='voyagesparbateau',
            name='dateAjout',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 11, 28, 11, 28, 52, 417926, tzinfo=utc), verbose_name="Date d'integration"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voyagesparbateau',
            name='dateModifiee',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AddField(
            model_name='voyagesparbu',
            name='dateAjout',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 11, 28, 11, 28, 57, 695995, tzinfo=utc), verbose_name="Date d'integration"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voyagesparbu',
            name='dateModifiee',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
    ]
