# Generated by Django 2.2.7 on 2020-07-09 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0003_auto_20200707_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_id', to='employee.Employee'),
        ),
    ]