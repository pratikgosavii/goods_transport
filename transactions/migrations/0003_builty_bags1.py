# Generated by Django 4.1.5 on 2023-04-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='builty',
            name='bags1',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
