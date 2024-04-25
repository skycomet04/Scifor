# Generated by Django 4.2.4 on 2024-04-11 02:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aapniparking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veh_model', models.CharField(max_length=255)),
                ('veh_registration_no', models.CharField(max_length=10)),
                ('owner_contactno', models.CharField(max_length=10)),
                ('parking_rate', models.PositiveIntegerField()),
                ('intime', models.DateTimeField(auto_now_add=True)),
                ('outtime', models.DateTimeField()),
                ('fee', models.FloatField()),
                ('vehicle_type', models.CharField(choices=[('4', '4-wheeler'), ('3', '3-wheeler'), ('2', '2-wheeler')], default='2', max_length=50)),
                ('owner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicleid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aapniparking.vehicle')),
            ],
        ),
        migrations.DeleteModel(
            name='Parking',
        ),
    ]