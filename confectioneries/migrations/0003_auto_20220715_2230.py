# Generated by Django 3.2.9 on 2022-07-16 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confectioneries', '0002_auto_20220616_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confectioneries',
            name='postingDate2',
        ),
        migrations.RemoveField(
            model_name='confectioneries',
            name='postingDate3',
        ),
        migrations.RemoveField(
            model_name='confectioneries',
            name='postingDate4',
        ),
    ]
