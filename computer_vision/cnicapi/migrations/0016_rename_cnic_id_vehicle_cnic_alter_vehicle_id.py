# Generated by Django 4.1.4 on 2022-12-25 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnicapi', '0015_remove_person_id_alter_person_cnic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='cnic_id',
            new_name='cnic',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]