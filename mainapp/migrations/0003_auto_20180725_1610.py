# Generated by Django 2.0.7 on 2018-07-25 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_markettable1_markettable2_markettable3_markettable4_markettable5_markettable6'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='markettable1',
            name='source_id',
        ),
        migrations.RemoveField(
            model_name='markettable2',
            name='source_id',
        ),
        migrations.RemoveField(
            model_name='markettable3',
            name='source_id',
        ),
        migrations.RemoveField(
            model_name='markettable4',
            name='source_id',
        ),
        migrations.RemoveField(
            model_name='markettable5',
            name='source_id',
        ),
        migrations.RemoveField(
            model_name='markettable6',
            name='source_id',
        ),
    ]
