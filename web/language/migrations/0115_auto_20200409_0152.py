# Generated by Django 2.2.8 on 2020-04-09 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0114_relateddata_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxonomy',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_taxonomies', to='language.Taxonomy'),
        ),
    ]
