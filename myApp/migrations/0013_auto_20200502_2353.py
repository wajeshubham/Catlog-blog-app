# Generated by Django 3.0.5 on 2020-05-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_auto_20200502_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_pics'),
        ),
    ]
