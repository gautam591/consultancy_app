from django.shortcuts import render,get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json
from django.conf import settings


@require_GET
def home(request):
   webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
   vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
   user = request.user
   return render(request, 'webPush/home.html', {user: user, 'vapid_key': vapid_key})

def send_push(request):
    #try:
    body = request.body
    
    data = {'push_head': request.POST.get('push_head'),
            'push_body': request.POST.get('push_body'),
            'id' : request.POST.get('id')
        }

    if 'push_head' not in data or 'push_body' not in data or 'id' not in data:
        return JsonResponse(status=400, data={"message": "Invalid data format"})

    user = request.user
    payload = {'head': data['push_head'], 'body': data['push_body']}
    send_user_notification(user=user, payload=payload, ttl=1000)

    return JsonResponse(status=200, data={"message": "Web push successful"})
    #except TypeError:
    #    print(">>> ERROR (TypeError) !! : ")
    #    return JsonResponse(status=500, data={"message": "An error occurred : TypeError"})
    #except Exception as exp:
    #    print(">>> ERROR !! : ",exp)
    #    return JsonResponse(status=500, data={"message": "An error occurred"})