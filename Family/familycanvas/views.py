from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from familycanvas.forms import create_group_form,login_form,reg_form,create_story,create_gallery,create_event


from familycanvas.models import story,gallery,events
# Create your views here.





@login_required
def home(request):
    return render(request,'familycanvas/home1.html',{})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def createGroupV(request):
    if request.method == "POST":
        form = create_group_form(request.POST)
        if form.is_valid():
            gname = form.cleaned_data['group_name']
            mail1 = form.cleaned_data['mem_mail1']
            mail2 = form.cleaned_data['mem_mail2']
            mail3 = form.cleaned_data['mem_mail3']
            mail4 = form.cleaned_data['mem_mail4']
            mail5 = form.cleaned_data['mem_mail5']
            mail6 = form.cleaned_data['mem_mail6']
            g = Group(name = gname)
            g.save()
            m1 = groups(gid = Group.objects.get(name=gname),email = mail1)
            m1.save()
            m2 = groups(gid = Group.objects.get(name=gname),email = mail2)
            m2.save()
            m3 = groups(gid = Group.objects.get(name=gname),email = mail3)
            m3.save()
            m4 = groups(gid = Group.objects.get(name=gname),email = mail4)
            m4.save()
            m5 = groups(gid = Group.objects.get(name=gname),email = mail5)
            m5.save()
            m6 = groups(gid = Group.objects.get(name=gname),email = mail6)
            m6.save()
            #return HttpResponseRedirect('/groupCreated.html')
    else:
        form = create_group_form()
    return render(request,'familycanvas/createGroup.html',{'form': form})

def groupCreatedV(request):
    return render(request,'familycanvas/groupCreated.html',{})
    
def registeredV(request):
    return render(request,'familycanvas/registered.html',{})

def login_formV(request):
    form = login_form()
    return render(request,'familycanvas/login.html',{'form': form})
    

    
@login_required
def create_storyV(request):
    if request.method == 'POST':
        form = create_story(request.POST, request.FILES)
        if form.is_valid():
            form.save()
          
            return render(request, 'familycanvas/createstory.html', {})
    else:
        form = create_story()
    return render(request, 'familycanvas/createstory.html', {'form': form})
@login_required    
def view_storyV(request):
    li = [ ];
    m = story.objects.all()
          #  for i in m:
          #      li.append(i.document)
           # return render(request, 'image/model_form_upload.html', {'li': li})
    return render(request, 'familycanvas/viewstory.html', {'li': m})
@login_required
def create_galleryV(request):
    if request.method == 'POST':
        form = create_gallery(request.POST, request.FILES)
        if form.is_valid():
            form.save()
          
            return render(request, 'familycanvas/gallery_create.html', {})
    else:
        form = create_gallery()
    return render(request, 'familycanvas/gallery_create.html', {'form': form})
    

@login_required
def view_galleryV(request):
    li = [ ];
    m = gallery.objects.all()
          #  for i in m:
          #      li.append(i.document)
           # return render(request, 'image/model_form_upload.html', {'li': li})
    return render(request, 'familycanvas/viewgallery.html', {'li': m})
@login_required    
def create_eventV(request):
    if request.method == 'POST':
        form = create_event(request.POST, request.FILES)
        if form.is_valid():
            form.save()
          
            return render(request, 'familycanvas/create_event.html', {})
    else:
        form = create_event()
    return render(request, 'familycanvas/create_event.html', {'form': form})
    
@login_required
def view_eventV(request):
    li = [ ];
    m = events.objects.all()
          #  for i in m:
          #      li.append(i.document)
           # return render(request, 'image/model_form_upload.html', {'li': li})
    return render(request, 'familycanvas/view_event.html', {'li': m})

def storyV(request):
    return render(request,'familycanvas/story.html',{})   

def eventV(request):
    return render(request,'familycanvas/event.html',{})         

def galleryV(request):
    return render(request,'familycanvas/gallery.html',{})      
    

