# Generated by Django 2.2.3 on 2019-07-14 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0025_auto_20190714_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lnadata',
            name='fluent_speakers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lnadata',
            name='learners',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lnadata',
            name='pop_off_res',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lnadata',
            name='pop_on_res',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lnadata',
            name='pop_total_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lnadata',
            name='some_speakers',
            field=models.IntegerField(default=0),
        ),
    ]
