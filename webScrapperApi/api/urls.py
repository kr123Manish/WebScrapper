from api.screenerEndpoints import screenEndpoints
from api.nseEndpoints import nseEndpoints
from django.urls import path

urlpatterns = [
   
    path('api/', screenEndpoints.ApiIsRunning),
    path('api/screener/data', screenEndpoints.Getdata),
    path('api/nse/data', nseEndpoints.Getdata)
]
