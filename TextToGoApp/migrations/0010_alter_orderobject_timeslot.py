# Generated by Django 3.2.10 on 2022-01-19 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextToGoApp', '0009_alter_orderobject_timeslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderobject',
            name='timeslot',
            field=models.CharField(choices=[('mon', '09:10 – 09:20'), ('tue', '09:20 – 09:30'), ('wed', '09:30 – 09:40'), ('thu', '09:40 – 09:50'), ('fri', '09:50 – 10:00')], max_length=256, null=True),
        ),
    ]