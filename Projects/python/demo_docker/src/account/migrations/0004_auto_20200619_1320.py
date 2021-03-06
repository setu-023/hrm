# Generated by Django 2.2.7 on 2020-06-19 13:20

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200618_1805'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='account',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='account',
            name='role',
        ),
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(default='  ', max_length=255),
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default='male', max_length=20),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(default='  ', max_length=255),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('archived', 'Archived'), ('deleted', 'Deleted')], default='active', max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
