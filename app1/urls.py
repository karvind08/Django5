from django.urls import path
from app1 import views
urlpatterns = [
    path('show/',views.show,name='show'),
    path('home/',views.home,name='home'),
    path('alldata',views.alldata,name='alldata'),
    path('single',views.singledata,name='single'),
    
]
