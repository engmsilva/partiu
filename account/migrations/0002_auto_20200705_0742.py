# Generated by Django 3.0.8 on 2020-07-05 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='value',
            new_name='balance',
        ),
        migrations.RemoveField(
            model_name='account',
            name='operation',
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=30)),
                ('value', models.FloatField(max_length=30)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='account.Account')),
            ],
        ),
    ]