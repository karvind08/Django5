from django.shortcuts import render

# Create your views here.

def app2fun(request):
    #html = '<h2>Messgae from App2 Fun with variable</h2>'
    # return HttpResponse('<h2>Messgae from App2 Fun</h2>')
    # syntax of render 
    #render(request,'template_name',context='Dic_name',content_type='MIME_Type',status=None,using=None)
    #return HttpResponse(html)
    return render(request,'app2/django.html')

def fastapi(request):
    return render(request,'app2/fastapi.html')
