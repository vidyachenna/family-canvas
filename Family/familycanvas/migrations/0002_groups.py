# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('familycanvas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('gid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
    ]
