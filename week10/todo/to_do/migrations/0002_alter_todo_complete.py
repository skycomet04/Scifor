# Generated by Django 4.2.4 on 2024-03-09 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]