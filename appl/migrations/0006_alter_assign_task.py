# Generated by Django 5.0.7 on 2024-07-28 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0005_alter_room_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assign',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='appl.task'),
        ),
    ]
