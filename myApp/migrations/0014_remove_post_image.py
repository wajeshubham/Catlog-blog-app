# Generated by Django 3.0.5 on 2020-05-02 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_auto_20200502_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
