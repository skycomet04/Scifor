# Generated by Django 4.2.4 on 2024-03-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_timestamp_alter_blog_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
