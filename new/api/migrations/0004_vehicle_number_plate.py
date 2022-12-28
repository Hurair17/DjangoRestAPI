# Generated by Django 4.1 on 2022-12-26 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_vehicle_id_imageupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='number_plate',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]