# Generated by Django 4.1.4 on 2022-12-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnicapi', '0011_alter_person_cnic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cnic',
            field=models.IntegerField(unique=True),
        ),
    ]