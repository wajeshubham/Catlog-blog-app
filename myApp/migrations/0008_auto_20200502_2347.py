# Generated by Django 3.0.5 on 2020-05-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_auto_20200502_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_images/'),
        ),
    ]