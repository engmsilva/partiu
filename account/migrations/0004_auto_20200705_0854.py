# Generated by Django 3.0.8 on 2020-07-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200705_0751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account_holder',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.FloatField(default=0, max_length=30, null=True),
        ),
    ]