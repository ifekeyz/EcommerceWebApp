# Generated by Django 3.2.9 on 2022-07-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuber', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuber',
            name='brief2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='tuber',
            name='brief3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='tuber',
            name='brief4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='tuber',
            name='description2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tuber',
            name='description3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tuber',
            name='description4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tuber',
            name='image2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='tuber',
            name='image3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='tuber',
            name='image4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='tuber',
            name='name2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='tuber',
            name='name3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='tuber',
            name='name4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='tuber',
            name='price2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='tuber',
            name='price3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='tuber',
            name='price4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='tuber',
            name='tag',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
