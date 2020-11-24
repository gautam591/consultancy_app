from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView
...
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

app_name = "webPush"
urlpatterns = [
    path('', views.home, name='home'),
    path('send_push', views.send_push, name='send_push'),
    path('sw.js/', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript'))    

   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
