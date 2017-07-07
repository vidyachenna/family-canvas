# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 05:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('familycanvas', '0004_auto_20170705_0417'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(default=1, upload_to='media/')),
                ('video', models.FileField(default=1, upload_to='media/')),
                ('gid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.RemoveField(
            model_name='gallery_pic',
            name='gid',
        ),
        migrations.RemoveField(
            model_name='gallery_video',
            name='gid',
        ),
        migrations.DeleteModel(
            name='gallery_pic',
        ),
        migrations.DeleteModel(
            name='gallery_video',
        ),
    ]
