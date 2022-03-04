# Generated by Django 3.2.10 on 2022-01-19 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextToGoApp', '0007_alter_orderobject_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderobject',
            name='timeslot',
            field=models.IntegerField(choices=[('09:10 – 09:20', '09:10 – 09:20'), ('09:20 – 09:30', '09:20 – 09:30'), (2, '09:30 – 09:40'), (3, '09:40 – 09:50'), (4, '09:50 – 10:00')], null=True),
        ),
    ]