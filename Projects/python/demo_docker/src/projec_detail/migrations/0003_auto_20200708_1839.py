# Generated by Django 2.2.7 on 2020-07-08 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projec_detail', '0002_auto_20200708_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectDetail', to='project.Project'),
        ),
    ]
