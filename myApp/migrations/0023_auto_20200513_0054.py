# Generated by Django 3.0.5 on 2020-05-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0022_auto_20200513_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
