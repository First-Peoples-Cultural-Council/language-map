# Generated by Django 2.2.13 on 2022-06-10 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0135_auto_20220513_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitymember',
            name='verified_by',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]