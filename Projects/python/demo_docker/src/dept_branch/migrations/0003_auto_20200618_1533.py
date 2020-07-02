# Generated by Django 2.2.7 on 2020-06-18 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dept_branch', '0002_auto_20200612_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deptbranch',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.Branch'),
        ),
        migrations.AlterField(
            model_name='deptbranch',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department'),
        ),
    ]