# Generated by Django 4.2.4 on 2024-03-29 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='doctor_ap_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='doctor',
            name='fees',
            field=models.IntegerField(default=350),
        ),
        migrations.AddField(
            model_name='doctor',
            name='resident',
            field=models.TextField(default=' '),
        ),
    ]