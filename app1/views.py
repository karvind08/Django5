from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show(request):
    return render(request,'app1/show.html')

def home(request):
    return render(request,'app1/home.html')