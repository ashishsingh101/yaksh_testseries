# Generated by Django 3.1.7 on 2021-10-11 05:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0054_auto_20211011_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 11, 5, 31, 46, 251365, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 11, 5, 31, 46, 251365, tzinfo=utc)),
        ),
    ]
