# Generated by Django 4.1.5 on 2024-03-10 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0030_alter_ack_history_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ack_history',
            name='update_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 3, 10, 10, 54, 57, 253444, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
