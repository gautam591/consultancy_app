from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
urlpatterns = [
    path('', include('axisCore.urls')),
    path('base/', include('axisPosts.urls')),
    path('users/', include('axisUsers.urls')),
    path('admin/', admin.site.urls),
    path('gautam/', include('webPush.urls')),
    path('webpush/', include('webpush.urls')),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript'))
]
#
