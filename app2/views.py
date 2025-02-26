from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2fun(request):
    html = '<h2>Messgae from App2 Fun with variable</h2>'
    # return HttpResponse('<h2>Messgae from App2 Fun</h2>')
    return HttpResponse(html)
