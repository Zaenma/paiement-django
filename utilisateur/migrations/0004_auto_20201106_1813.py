# Generated by Django 3.1.2 on 2020-11-06 18:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0003_auto_20201105_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsablesagence',
            name='id',
        ),
        migrations.AddField(
            model_name='responsablesagence',
            name='utilisateur_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='utilisateur.utilisateur'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='condition',
            field=models.BooleanField(default=1, verbose_name="Condition d'utilisation"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name="Date d'enregistrement"),
            preserve_default=False,
        ),
    ]