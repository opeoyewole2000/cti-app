# Generated by Django 2.0.7 on 2018-07-26 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_ctirawtable_file_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ctirawtable',
            name='date',
        ),
        migrations.RemoveField(
            model_name='ctirawtable',
            name='description',
        ),
        migrations.RemoveField(
            model_name='ctirawtable',
            name='label',
        ),
    ]