# Generated by Django 3.0.5 on 2020-05-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0030_auto_20200519_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]