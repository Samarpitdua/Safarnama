# Generated by Django 4.1.4 on 2022-12-29 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_profile_remove_hotels_destination_alter_image_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_of_rooms',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
