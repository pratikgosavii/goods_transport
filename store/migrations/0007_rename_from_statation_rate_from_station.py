# Generated by Django 4.1.5 on 2023-03-04 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_rates_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='from_statation',
            new_name='from_station',
        ),
    ]
