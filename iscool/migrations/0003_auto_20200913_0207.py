# Generated by Django 3.0.3 on 2020-09-13 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iscool', '0002_auto_20200913_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Nome'),
        ),
    ]
