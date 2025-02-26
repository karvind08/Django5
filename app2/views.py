from django.shortcuts import render

# Create your views here.

def app2fun(request):
    #html = '<h2>Messgae from App2 Fun with variable</h2>'
    # return HttpResponse('<h2>Messgae from App2 Fun</h2>')
    # syntax of render 
    #render(request,'template_name',context='Dic_name',content_type='MIME_Type',status=None,using=None)
    #return HttpResponse(html)
    c1 = {'cname':'Django 5'}
    return render(request,'app2/django.html',context=c1)

def fastapi(request):
    f1 = {'c1':'C++'}
    return render(request,'app2/fastapi.html',context=f1)
