# Generated by Django 3.0.5 on 2020-05-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0019_auto_20200512_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=True, upload_to='post_image'),
            preserve_default=False,
        ),
    ]
