# Generated by Django 4.1.4 on 2022-12-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_image_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='state',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
