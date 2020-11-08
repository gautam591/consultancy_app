# axisCore
from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView

app_name = "axisCore"
urlpatterns = [
    path('', views.base, name='base'),
    path('base1/', views.base1, name='base1'),
    path('base2/', views.base2, name='base2'),
    path('apply/', views.apply, name='apply'),

]
