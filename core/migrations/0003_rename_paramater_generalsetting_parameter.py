# Generated by Django 4.2.2 on 2023-06-26 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_generalsettings_generalsetting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generalsetting',
            old_name='paramater',
            new_name='parameter',
        ),
    ]
