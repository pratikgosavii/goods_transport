# Generated by Django 4.1.5 on 2023-03-11 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_drivers_details_driver'),
        ('transactions', '0006_remove_builty_challan_date_ack_challan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='builty',
            name='less_tds',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='builty',
            name='note',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='builty',
            name='petrol_pump',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wdsfgv', to='store.petrol_pump'),
        ),
    ]
