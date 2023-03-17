# Generated by Django 4.1.5 on 2023-03-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_petrol_pump'),
    ]

    operations = [
        migrations.CreateModel(
            name='drivers_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('address', models.CharField(max_length=120, unique=True)),
                ('adhar_card', models.CharField(max_length=120, unique=True)),
                ('mobile_no', models.IntegerField()),
            ],
        ),
    ]
