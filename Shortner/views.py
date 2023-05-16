from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import random
from .models import URL

def Home(request):
    return render(request, 'home.html')

def link_gen(request):
    link = request.GET.get('url')
    print(link)
    lst = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    while True:
        new = "".join(random.sample(lst, 5))
        if not URL.objects.filter(short=new).exists():
            link_saver = URL(short=new, olink=link)
            link_saver.save()
            break
    print(new)
    return JsonResponse({'link' : new})

def navigator(request,link):
    print(link)
    olink = URL.objects.filter(short=link).first()
    print(olink.olink)
    return redirect(olink.olink)