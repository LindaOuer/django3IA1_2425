# Generated by Django 4.2 on 2024-10-04 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferenceApp', '0001_initial'),
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferenceApp.conference')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='reservations',
            field=models.ManyToManyField(related_name='reservations', through='userApp.Reservation', to='conferenceApp.conference'),
        ),
    ]