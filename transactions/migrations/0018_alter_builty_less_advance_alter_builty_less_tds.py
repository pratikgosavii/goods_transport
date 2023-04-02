# Generated by Django 4.1.5 on 2023-04-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0017_alter_builty_less_advance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='builty',
            name='less_advance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='builty',
            name='less_tds',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
