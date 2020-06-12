# Generated by Django 2.2.7 on 2020-06-12 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeptBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('total_emplooye', models.IntegerField(default=0)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='branch.Branch')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='department.Department')),
            ],
            options={
                'db_table': 'DeptBranches',
            },
        ),
    ]
