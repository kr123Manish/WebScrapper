from api import views
from django.urls import path

urlpatterns = [
   
    path('api/', views.ApiIsRunning),
    path('api/data', views.Getdata)
]
