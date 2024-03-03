# Generated by Django 4.1.5 on 2024-02-17 09:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0013_remove_builty_expense_date_remove_other_expense_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='builty_expense',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='other_expense',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='salary',
            name='entry_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='truck_expense',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
