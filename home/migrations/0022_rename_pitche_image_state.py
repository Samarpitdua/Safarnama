# Generated by Django 4.1.4 on 2022-12-29 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_image_state_image_pitche'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='pitche',
            new_name='state',
        ),
    ]
