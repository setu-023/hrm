# Generated by Django 2.2.7 on 2020-07-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='month',
            field=models.DateTimeField(),
        ),
    ]