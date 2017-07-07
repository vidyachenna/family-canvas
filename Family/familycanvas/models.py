from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

# Create your models here.

"""class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    user_pic = models.ImageField(upload_to = 'profile/',default = 1)
@receiver(post_save,sender = User)
def create_user_profile(sender,instance,created,**kwargs):
        if created:
            profile.objects.create(user = instance)
@receiver(post_save,sender = User)
def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()"""


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    user_pic = models.CharField(max_length = 150,null = True)
@receiver(post_save,sender = User)
def create_user_profile(sender,instance,created,**kwargs):
        if created:
            profile.objects.create(user = instance)
@receiver(post_save,sender = User)
def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()

class story(models.Model):
    uid = models.ForeignKey(User, default = 1)
    gid = models.ForeignKey(Group,default = 1)
    storyline = models.TextField()
    track = models.FileField(upload_to ='media/audio_story/',default = 1)
    

class events(models.Model):
    uid = models.ForeignKey(User, default = 1)
    gid = models.ForeignKey(Group,default = 1)
    event_title =  models.CharField(max_length = 150,default = None)
    event_text = models.TextField()
    event_track = models.FileField(upload_to = 'media/audio_event/',default = 1)
    event_video = models.FileField(upload_to = 'media/video_event/',default = 1)
    event_img = models.FileField(upload_to = 'media/Event/',default = 1)
    def __str__(self):
        return self.uid
class gallery(models.Model):
    gid = models.ForeignKey(Group,default = 1)
    pic = models.FileField(upload_to = 'media/',default = 1)
    video = models.FileField(upload_to = 'media/',default = 1)
    def __str__(self):
        return self.gid
                                                                                                                      
    def __str__(self):
        return self.gid
class Family_tree(models.Model):
    gid = models.ForeignKey(Group,default = 1)
    treepic = models.ImageField(upload_to = 'media/ftree_pic/',default = 1)
    def __str__(self):
        return self.gid
class group_names(models.Model):
    groupname = models.CharField(max_length =50)
class groups(models.Model):
    gid = models.ForeignKey(group_names,default =None)
    email = models.EmailField()
