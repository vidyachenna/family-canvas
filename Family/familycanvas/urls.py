from django.conf.urls import url
from familycanvas import views
urlpatterns = [
        url(r'^home$',views.home,name = 'home'),
        url(r'^createGroup$',views.createGroupV,name = 'createGroup'),
        url(r'^groupCreated$',views.groupCreatedV,name = 'groupCreated'),
        url(r'^registered$',views.registeredV,name = 'registered'),
        url(r'^login$',views.login_formV,name = 'login_form'),
        url(r'^register$',views.reg_formV,name = 'reg_form'),
]
