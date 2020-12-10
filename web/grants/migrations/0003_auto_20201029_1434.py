# Generated by Django 2.2.8 on 2020-10-29 14:34
import csv

from django.db import migrations, models

from grants.management.commands.migrate_manytomany_fields import migrate_manytomany_fields


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0002_auto_20201022_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='communities_affiliations',
            field=models.ManyToManyField(blank=True, related_name='grants', to='language.Community', verbose_name='Communities/Affiliations'),
        ),
        migrations.AddField(
            model_name='grant',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='grants', to='language.Language'),
        ),
        migrations.AddField(
            model_name='grant',
            name='recipients',
            field=models.ManyToManyField(blank=True, related_name='grants', to='language.PlaceName'),
        )
    ]