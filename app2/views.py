from django.shortcuts import render
from app2.forms import Registeration,Login
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
    d1 = {'c3':"Streamlit"}
    #return render(request,'app2/fastapi.html',context=f1)
    #return render(request,'app2/fastapi.html',context={'c2':'Python'})
    return render(request,'app2/fastapi.html',d1)

#def register(request):
#    fm = Registeration()
#    return render(request,'app2/register.html',{'form':fm})

def register(request):
    fm = Registeration(field_order=['city','email','first_name','last_name'])
    return render(request,'app2/register.html',{'form':fm})


def login(request):
    #fm = Login(auto_id='arv_%s')
    #fm = Login(auto_id=True)
    fm = Login(auto_id=False)
    return render(request,'app2/login.html',{'form':fm})