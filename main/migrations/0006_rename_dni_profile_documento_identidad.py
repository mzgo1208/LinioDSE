# Generated by Django 3.2.4 on 2021-06-06 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210605_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='dni',
            new_name='documento_identidad',
        ),
    ]
