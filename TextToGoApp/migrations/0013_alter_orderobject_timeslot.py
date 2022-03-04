# Generated by Django 3.2.10 on 2022-01-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextToGoApp', '0012_example'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderobject',
            name='timeslot',
            field=models.TimeField(choices=[('09:10', '09:10 – 09:20'), ('09:20', '09:20 – 09:30'), ('09:30', '09:30 – 09:40'), ('09:40', '09:40 – 09:50'), ('09:50', '09:50 – 10:00')], max_length=256, null=True),
        ),
    ]
