# Generated by Django 2.2.7 on 2020-06-27 14:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200619_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='groups',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, null=True, size=None),
        ),
    ]