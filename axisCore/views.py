# axisCore
from django.shortcuts import render
#from django.http import HttpResponse
#from django.http import JsonResponse

#from django.contrib import messages

def base(request):
    #template = loader.get_template('axisCore/base.html')
    context = {'base':'base'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisCore/base.html', context)
def base1(request):
    #template = loader.get_template('axisCore/base.html')
    context = {'base1':'base1'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisCore/base1.html', context)

def base2(request):
    #template = loader.get_template('axisCore/base.html')
    context = {'base2':'base2'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisCore/base2.html', context)