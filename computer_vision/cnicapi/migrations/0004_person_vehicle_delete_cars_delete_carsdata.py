# Generated by Django 4.1.4 on 2022-12-23 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cnicapi', '0003_rename_cart_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnic', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cnic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cnicapi.person')),
            ],
            options={
                'ordering': ['cnic_id', '-created_at'],
            },
        ),
        migrations.DeleteModel(
            name='Cars',
        ),
        migrations.DeleteModel(
            name='CarsData',
        ),
    ]
