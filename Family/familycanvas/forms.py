from django import forms
from django.contrib.auth.models import User
from familycanvas.models import story,events,gallery

class create_group_form(forms.Form):
    group_name = forms.CharField(max_length = 150)
    mem_mail1 = forms.EmailField()
    mem_mail2 = forms.EmailField()
    mem_mail3 = forms.EmailField()
    mem_mail4 = forms.EmailField()
    mem_mail5 = forms.EmailField()
    mem_mail6 = forms.EmailField()

class login_form(forms.Form):
    user_name = forms.EmailField()
    pwd = forms.CharField(max_length = 8,min_length = 6)

class reg_form(forms.Form):
    user_name = forms.CharField(max_length = 150,min_length = 3)
    pwd = forms.CharField(max_length = 8,min_length = 6,widget = forms.PasswordInput())
    #confirm_pwd = forms.CharField(max_length = 8,min_length = 6)
    mail_id = forms.EmailField()

class create_story(forms.ModelForm):
     class Meta:
        model = story
        fields = ('storyline', 'track', )  
        
class create_gallery(forms.ModelForm):
    class Meta:
        model = gallery
        fields = ('pic','video',)  
        
class create_event(forms.ModelForm):
     class Meta:
        model = events
        fields = ('event_title','event_text','event_track','event_video','event_img' )          
          
    

