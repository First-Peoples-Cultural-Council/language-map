# Generated by Django 2.2.4 on 2019-08-16 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0050_auto_20190815_0752'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceNameCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('icon_name', models.CharField(default=None, max_length=32, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='media',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='placename',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='language.PlaceNameCategory'),
        ),
    ]