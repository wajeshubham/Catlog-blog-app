# Generated by Django 3.0.5 on 2020-05-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0017_auto_20200506_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=True, upload_to='post_image'),
            preserve_default=False,
        ),
    ]
