# Generated by Django 3.0.8 on 2020-07-04 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]
