# Generated by Django 5.0.7 on 2024-07-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0004_alter_profile_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='rooms/'),
        ),
    ]
