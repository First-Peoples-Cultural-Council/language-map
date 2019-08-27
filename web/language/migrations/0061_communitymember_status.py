# Generated by Django 2.2.4 on 2019-08-27 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0060_communitymember_languagemember'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitymember',
            name='status',
            field=models.CharField(choices=[('PE', 'Pendant'), ('VE', 'Verified'), ('RE', 'Rejected')], default='PE', max_length=2),
        ),
    ]
