# Generated by Django 4.2.4 on 2024-03-17 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import to_do.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do', '0003_rename_complete_todo_completed_alter_todo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='creator',
            field=models.ForeignKey(default=to_do.models.get_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
