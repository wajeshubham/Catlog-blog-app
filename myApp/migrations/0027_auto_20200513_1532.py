# Generated by Django 3.0.5 on 2020-05-13 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0026_auto_20200513_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=250, verbose_name='message'),
        ),
    ]
