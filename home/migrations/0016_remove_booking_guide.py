# Generated by Django 4.1.4 on 2022-12-29 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_booking_guide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='guide',
        ),
    ]
