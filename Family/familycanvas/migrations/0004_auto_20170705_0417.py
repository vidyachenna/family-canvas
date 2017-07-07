# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 04:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('familycanvas', '0003_auto_20170704_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='group_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_pic', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='events',
            name='event_img',
            field=models.ImageField(default=1, upload_to='media/Event/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_track',
            field=models.FileField(default=1, upload_to='media/audio_event/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_video',
            field=models.FileField(default=1, upload_to='media/video_event/'),
        ),
        migrations.AlterField(
            model_name='family_tree',
            name='treepic',
            field=models.ImageField(default=1, upload_to='media/ftree_pic/'),
        ),
        migrations.AlterField(
            model_name='gallery_pic',
            name='pic',
            field=models.ImageField(default=1, upload_to='media/Gallery_photo/'),
        ),
        migrations.AlterField(
            model_name='gallery_video',
            name='video',
            field=models.FileField(default=1, upload_to='media/Gallery_vid/'),
        ),
        migrations.AlterField(
            model_name='groups',
            name='gid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='familycanvas.group_names'),
        ),
        migrations.AlterField(
            model_name='story',
            name='track',
            field=models.FileField(default=1, upload_to='media/audio_story/'),
        ),
    ]
