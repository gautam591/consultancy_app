# axisCore
from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
app_name = "axisCore"
urlpatterns = [
    path('', views.base, name='base'),
    path('base1/', views.base1, name='base1'),
    path('base2/', views.base2, name='base2'),
    path('baseadmin/', views.baseadmin, name='baseadmin'),
    path('seminar/', views.seminar, name='seminar'),
    path('seminarondb/', views.seminarondb, name='seminarondb'),
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

