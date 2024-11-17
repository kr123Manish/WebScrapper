from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse

from api import program as p


def ApiIsRunning(request):
    return JsonResponse({"message":"Web Scrapper api is running."})

def Getdata(request):
    obj = p.WebScrapper("tcs")

    status = obj.getStatus()
    if status == 200:

        titles = obj.getTitles()
        aboutSection = obj.aboutSection()
        topRatios = obj.topRatios()
        analysis = obj.analysis()

        data = {
            "status": status,
            "titles": titles,
            "aboutSection": aboutSection,
            "topRatios": topRatios,
            "analysis": {
                "pros":analysis[0],
                "cons":analysis[1]
            },
        }

        return JsonResponse(data)
    else:
        return JsonResponse({"message": "Company not found please check."})