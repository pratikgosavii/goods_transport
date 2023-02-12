# Generated by Django 4.1.5 on 2023-01-31 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truck_owner',
            name='truck',
        ),
        migrations.AddField(
            model_name='truck_details',
            name='truck_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ddfdf', to='store.truck_owner'),
            preserve_default=False,
        ),
    ]
