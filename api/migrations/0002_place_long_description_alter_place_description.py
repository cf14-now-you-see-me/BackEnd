# Generated by Django 4.1 on 2022-10-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='long_description',
            field=models.CharField(default='', max_length=4096),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(max_length=2048),
        ),
    ]
