# axisCore
from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'axisUsers'

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('goback/', views.goback, name='goback'),
    path('register/', views.register, name='register'),
    path('update/', views.updateUserProfile, name='updateUserProfile'),
    path('profile/', views.viewProfile, name='profile'),
    path('terms/', views.terms, name='termsAndConditions'),
    path('gautam/', views.gautam, name='gautam'),
    path('searchstudentinfo/', views.searchstudentinfo, name='searchstudentinfo'),
    path('searchclassinfo/', views.searchclassinfo, name='searchclassinfo'),
    path('passadmin/', views.passadmin, name='passadmin'),
    path('studentinformation/', views.studentinformation, name='studentinformation'),
    path('classinformation/', views.classinformation, name='classinformation'),
    path('seminarinformation/', views.seminarinformation, name='seminarinformation'),
    
]
