# Generated by Django 2.2.7 on 2020-06-12 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dept_branch', '0002_auto_20200612_0601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('possition', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=25, unique=True)),
                ('address', models.TextField()),
                ('dob', models.CharField(max_length=25, unique=True)),
                ('joining_date', models.DateTimeField(verbose_name='joining date')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('posting', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dept_branch.DeptBranch')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]