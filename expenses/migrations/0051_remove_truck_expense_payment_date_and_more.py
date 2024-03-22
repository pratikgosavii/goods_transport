# Generated by Django 4.1.5 on 2024-03-22 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0050_remove_transfer_fund_payment_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truck_expense',
            name='payment_date',
        ),
        migrations.AlterField(
            model_name='builty_expense',
            name='entry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 22, 15, 33, 54, 693659, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='diesel_expense',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 15, 33, 54, 693659, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='fund',
            name='entry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 22, 15, 33, 54, 693659, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='other_expense',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 15, 33, 54, 693659, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='salary',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 15, 33, 54, 693659, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='transfer_fund',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 15, 33, 54, 693659, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='truck_diesel_expense',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 15, 33, 54, 693659, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='truck_expense',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 15, 33, 54, 693659, tzinfo=datetime.timezone.utc)),
        ),
    ]
