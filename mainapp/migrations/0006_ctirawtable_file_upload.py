# Generated by Django 2.0.7 on 2018-07-25 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20180725_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctirawtable',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]