from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('axisCore.urls')),
    path('base/', include('axisPosts.urls')),
    path('users/', include('axisUsers.urls')),
    path('admin/', admin.site.urls),
]
#
