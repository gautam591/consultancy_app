# axisCore
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import seminarForm
from axisPosts.models import Post,postReactions,postComments,commentReactions
from axisUsers.models import User
#from django.http import HttpResponse
#from django.http import JsonResponse

#from django.contrib import messages

def base(request):
    #template = loader.get_template('axisCore/base.html')
    context = {'base':'base'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisCore/base.html', context)

def baseadmin(request):
    model = Post.objects.all()
    postPG = Paginator(model, 10)
    firstPage = postPG.get_page(1)
    #pageRange = postPG.page_range
    postIds = [x.id for x in firstPage]
    if request.user.is_authenticated:
        postRcs = postReactions.objects.filter(postId__in=postIds,userName=request.user)[:10]
    else :
        postRcs =[]
    app = 'axisPosts'
    context = {'post_list': firstPage,'reaction_list':postRcs,'page_n':1,'app_name':app}

    if request.method == 'POST':
        page_n = int(request.POST.get('page_n', None))
        page_n += 1
        results = postPG.get_page(page_n)
        postIds = [x.id for x in results]
        if request.user.is_authenticated:
            postRcs = postReactions.objects.filter(postId__in=postIds,userName=request.user)[:10]
        else :
            postRcs =[]
        context = {'post_list': results,'reaction_list':postRcs,'page_n':page_n}
        return render(request, 'axisPosts/postList.html',context) 

    return render(request,'axisPosts/postadmin.html',context) 

def passadmin(request):
    #template = loader.get_template('axisCore/base.html')
    context = {'passadmin':'passadmin'}
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisCore/passadmin.html', context)

def seminar(request):
    #template = loader.get_template('axisCore/base.html')
    
    #return HttpResponse(template.render(context,request))
    return render(request, 'axisCore/seminar.html', {'seminarForm':seminarForm()})

def seminarondb(request):
    if request.method == "POST":
        form = seminarForm(request.POST)
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.save()
            return redirect("axiscore:base2")

        else:
            return JsonResponse({'Error':True,'Errors':form.errors})
    else:
        form = seminarForm()
    return render(request, 'axisPosts/seminar.html',{'seminarForm':form})



def base1(request):
    model = Post.objects.all()
    postPG = Paginator(model, 10)
    firstPage = postPG.get_page(1)
    #pageRange = postPG.page_range
    postIds = [x.id for x in firstPage]
    if request.user.is_authenticated:
        postRcs = postReactions.objects.filter(postId__in=postIds,userName=request.user)[:10]
    else :
        postRcs =[]
    app = 'axisPosts'
    context = {'post_list': firstPage,'reaction_list':postRcs,'page_n':1,'app_name':app}

    if request.method == 'POST':
        page_n = int(request.POST.get('page_n', None))
        page_n += 1
        results = postPG.get_page(page_n)
        postIds = [x.id for x in results]
        if request.user.is_authenticated:
            postRcs = postReactions.objects.filter(postId__in=postIds,userName=request.user)[:10]
        else :
            postRcs =[]
        context = {'post_list': results,'reaction_list':postRcs,'page_n':page_n}
        return render(request, 'axisPosts/postList.html',context) 

    return render(request,'axisPosts/post.html',context) 

def base2(request):
    model = Post.objects.all()
    postPG = Paginator(model, 10)
    firstPage = postPG.get_page(1)
    #pageRange = postPG.page_range
    postIds = [x.id for x in firstPage]
    if request.user.is_authenticated:
        postRcs = postReactions.objects.filter(postId__in=postIds,userName=request.user)[:10]
    else :
        postRcs =[]
    app = 'axisPosts'
    context = {'post_list': firstPage,'reaction_list':postRcs,'page_n':1,'app_name':app}

    if request.method == 'POST':
        page_n = int(request.POST.get('page_n', None))
        page_n += 1
        results = postPG.get_page(page_n)
        postIds = [x.id for x in results]
        if request.user.is_authenticated:
            postRcs = postReactions.objects.filter(postId__in=postIds,userName=request.user)[:10]
        else :
            postRcs =[]
        context = {'post_list': results,'reaction_list':postRcs,'page_n':page_n}
        return render(request, 'axisPosts/postList.html',context) 

    return render(request,'axisPosts/post2.html',context) 