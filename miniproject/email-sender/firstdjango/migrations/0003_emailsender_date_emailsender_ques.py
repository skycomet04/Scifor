# Generated by Django 4.2.4 on 2024-03-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstdjango', '0002_emailsender_delete_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsender',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='emailsender',
            name='ques',
            field=models.TextField(null=True),
        ),
    ]
