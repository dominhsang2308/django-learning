from django.urls import path

from myfirstdjango import settings
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('',views.myfunctioncall, name="index"),
    path('about',views.myfunctionabout, name="about"),
    path('intro/<str:name>/<int:age>',views.myfuncintro, name="intro"),
    path('myfirstpage', views.myfirstpage, name='myfirstpage'),
    path('mysecondpage', views.mysecondpage, name='mysecondpage'),
    path('mythirdpage', views.mythirdpage, name='mythirdpage'),
    path('myimagepage', views.myimgpage, name='myimagepage'),
    path('myimagepage2/<str:imgname>', views.myimgpage2, name='myimagepage2'),
    path('myform', views.myform, name='myform'),
    path('submitmyform', views.submitmyform, name='submitmyform'),
    path('myform2', views.myform2, name='myform2')
] 