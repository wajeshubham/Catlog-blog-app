# Generated by Django 3.0.5 on 2020-05-12 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0025_auto_20200513_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=250),
        ),
    ]