from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('axisCore.urls')),
    path('base/', include('axisPosts.urls')),
    path('users/', include('axisUsers.urls')),
    path('admin/', admin.site.urls),
    path('webPush/', include('webPush.urls')),
    path('webpush/', include('webpush.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
