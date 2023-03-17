# Generated by Django 4.1.5 on 2023-03-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_truck_owner_truck_truck_details_truck_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck_details',
            name='fitness',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='truck_details',
            name='insurance_number',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='truck_details',
            name='permit_number',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='truck_details',
            name='puc_number',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='truck_owner',
            name='address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='truck_owner',
            name='bank_acc',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='truck_owner',
            name='mobile_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
