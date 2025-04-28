from django.http import HttpResponse
from django.shortcuts import render
from visitors.models import PageVisit



def homeView(request,*args,**kargs):
    return AboutView(request,*args,**kargs)


def AboutView(request,*args,**kargs):

    
    qs=PageVisit.objects.all()
    page_qs=PageVisit.objects.filter(path=request.path)
    my_title="about"
    try:
        percent=page_qs.count() * 100 /qs.count()
    except:
        percent=0
    mycontent={
        "page_title":my_title,
        "pageVisitCount":page_qs.count(),
        "totalVisitCount":qs.count(),
        "percent":percent
    }
    # print("path",request.path)

    html_templates="home.html"
    PageVisit.objects.create(path=request.path)
    return render(request,html_templates,mycontent)