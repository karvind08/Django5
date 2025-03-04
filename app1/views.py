from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Profile

# Create your views here.
def show(request):
    return render(request,'app1/show.html')

def home(request):
    return render(request,'app1/home.html')

def alldata(request):
    data = Profile.objects.all()
    print(data)
    return render(request,'app1/all-data.html',{'data':data})

def singledata(request):
    data1= Profile.objects.get(id=0)
    print(data1)
    return render(request,'app1/single.html',{'data1':data1})