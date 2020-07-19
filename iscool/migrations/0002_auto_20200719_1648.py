# Generated by Django 3.0.3 on 2020-07-19 19:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iscool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliationmodel',
            name='note',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(20)]),
        ),
    ]