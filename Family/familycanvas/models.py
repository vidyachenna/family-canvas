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

class story(models.Model):
    uid = models.ForeignKey(User, default = 1)
    gid = models.ForeignKey(Group,default = 1)
    storyline = models.TextField()
    track = models.FileField(upload_to ='audio_story/',default = 1)
    def __str__(self):
        return self.gid
class event_details(models.Model):
    event_name = models.CharField(max_length = 50)
    def __str__(self):
        return self.event_name
class events(models.Model):
    uid = models.ForeignKey(User, default = 1)
    gid = models.ForeignKey(Group,default = 1)
    event_id =  models.ForeignKey(event_details)
    event_text = models.TextField()
    event_track = models.FileField(upload_to = 'audio_event/',default = 1)
    event_video = models.FileField(upload_to = 'video_event/',default = 1)
    event_img = models.ImageField(upload_to = 'Event/',default = 1)
    def __str__(self):
        return self.uid
class gallery_pic(models.Model):
    gid = models.ForeignKey(Group,default = 1)
    pic = models.ImageField(upload_to = 'Gallery_photo/',default = 1)
    def __str__(self):
        return self.gid
class gallery_video(models.Model):
    gid = models.ForeignKey(Group,default = 1)
    video = models.FileField(upload_to = 'Gallery_vid/',default = 1)
    def __str__(self):
        return self.gid
class Family_tree(models.Model):
    gid = models.ForeignKey(Group,default = 1)
    treepic = models.ImageField(upload_to = 'ftree_pic/',default = 1)
    def __str__(self):
        return self.gid
class groups(models.Model):
    gid = models.ForeignKey(Group,default =None)
    email = models.EmailField()
    def __str__(self):
        return self.email
