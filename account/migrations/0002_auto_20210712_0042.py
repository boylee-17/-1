# Generated by Django 3.2.5 on 2021-07-11 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='nickmane',
            new_name='nickname',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='universuty',
            new_name='university',
        ),
    ]
