# Generated by Django 5.0.7 on 2024-07-28 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0007_alter_assign_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assign',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appl.task'),
        ),
    ]