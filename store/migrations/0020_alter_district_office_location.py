# Generated by Django 4.1.5 on 2023-04-02 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_district_office_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='office_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.office_location'),
            preserve_default=False,
        ),
    ]
