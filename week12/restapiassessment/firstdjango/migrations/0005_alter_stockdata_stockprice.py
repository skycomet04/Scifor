# Generated by Django 4.2.4 on 2024-04-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstdjango', '0004_stockdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdata',
            name='stockprice',
            field=models.FloatField(),
        ),
    ]
