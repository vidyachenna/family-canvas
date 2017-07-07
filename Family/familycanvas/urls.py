from django.conf.urls import url

from django.contrib import admin
from django.contrib.auth import views as auth_views

from familycanvas import views as familycanvas_views

from familycanvas import views
urlpatterns = [
        url(r'^login/$', auth_views.login,{'template_name': 'registration/login.html'},  name='login'),
        url(r'^logout/$', auth_views.logout, name='logout'),
        url(r'^signup/$',familycanvas_views.signup,name = 'signup'),
        
        
        url(r'^home/$',views.home,name = 'home'),
        url(r'^createGroup/',views.createGroupV,name = 'createGroup'),
        url(r'^groupCreated$',views.groupCreatedV,name = 'groupCreated'),
        url(r'^registered$',views.registeredV,name = 'registered'),
        #url(r'^login$',views.login_formV,name = 'login_form'),
        #url(r'^register$',views.reg_formV,name = 'reg_form'),
        url(r'^story$',views.storyV,name = 'story'),
        url(r'^createstory$',views.create_storyV,name = 'story_form'),
        url(r'^viewstory/$',views.view_storyV,name = 'story_view'),
        
        url(r'^event$',views.eventV,name = 'event'),
        url(r'^createevent$',views.create_eventV,name = 'event_form'),
        url(r'^viewevent$',views.view_eventV,name = 'event_view'),
        
        url(r'^gallery$',views.galleryV,name = 'gallery'),
	    url(r'^creategallery$',views.create_galleryV,name = 'gallery_form'),
	    url(r'^viewgallery$',views.view_galleryV,name = 'gallery_view'),
	    
        url(r'^admin/', admin.site.urls),

]
