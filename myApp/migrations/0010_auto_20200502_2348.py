# Generated by Django 3.0.5 on 2020-05-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_auto_20200502_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=1, upload_to='post_images/'),
            preserve_default=False,
        ),
    ]
