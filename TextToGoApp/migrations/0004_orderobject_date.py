# Generated by Django 3.2.10 on 2022-01-17 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextToGoApp', '0003_auto_20220116_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderobject',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]