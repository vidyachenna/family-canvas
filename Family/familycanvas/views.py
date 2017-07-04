from django.shortcuts import render
from django.http import HttpResponseRedirect
from familycanvas.forms import create_group_form,login_form,reg_form
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'familycanvas/home1.html',{})

def createGroupV(request):
    form = create_group_form()
    return render(request,'familycanvas/createGroup.html',{'form': form})

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
    
def reg_formV(request):
    if request.method == "POST":
        form = reg_form(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            pwd = form.cleaned_data['pwd']
            mail_id = form.cleaned_data['mail_id']
            print(user_name+"vijju")
            user = User(username = user_name,password = pwd,email = mail_id)
            user.save()
    else:
        form = reg_form()
    return render(request,'familycanvas/register.html',{'form': form})
    

