# Generated by Django 4.1.5 on 2023-04-09 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_adhar_card_driver_adhar_card1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='adhar_card1',
            new_name='adhar_card',
        ),
    ]
