from django.urls import path,include
from app2 import views

urlpatterns = [
   
    path('app2fun/',views.app2fun,name='appfun'),  
    path('fastapi/',views.fastapi,name='fastapi'),
    path('register/',views.register,name='register'),
]
