# Generated by Django 5.1.6 on 2025-02-21 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_customuser_group_delete_usergroup'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group'),
        ),
    ]
