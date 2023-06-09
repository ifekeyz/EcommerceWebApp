# Generated by Django 3.2.9 on 2022-07-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('untensils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='untensiles',
            name='brief2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='brief3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='brief4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='description2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='description3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='description4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='image2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='image3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='image4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='name2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='name3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='name4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='price2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='price3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='price4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='untensiles',
            name='tag',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
