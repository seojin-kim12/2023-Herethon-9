# Generated by Django 3.2.20 on 2023-07-11 14:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 11, 14, 22, 41, 941917, tzinfo=utc)),
        ),
    ]
