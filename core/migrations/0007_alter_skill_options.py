# Generated by Django 4.2.2 on 2023-06-27 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('order',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]
