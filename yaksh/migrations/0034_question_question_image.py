# Generated by Django 3.2 on 2021-07-19 15:53

from django.db import migrations, models
import yaksh.models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0033_alter_profile_timezone'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='question_image/', validators=[yaksh.models.validate_image]),
        ),
    ]
