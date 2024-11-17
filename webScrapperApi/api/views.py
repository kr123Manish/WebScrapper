from django.http.response import JsonResponse
from api import program as p  # Import your WebScrapper class


def ApiIsRunning(request):
    return JsonResponse({"message": "Web Scrapper API is running."})


def Getdata(request):
    company_name = request.GET.get('companyName')
    if not company_name:
        return JsonResponse({"error": "companyName parameter is required"}, status=400)

    try:
        
        obj = p.WebScrapper(company_name)

        
        status = obj.getStatus()
        if status != 200:
            return JsonResponse({"message": "Company not found, please check."}, status=404)

        
        try:
            titles = obj.getTitles()
        except Exception as e:
            titles = f"Error fetching titles: {str(e)}"

        try:
            about_section = obj.aboutSection()
        except Exception as e:
            about_section = f"Error fetching about section: {str(e)}"

        try:
            top_ratios = obj.topRatios()
        except Exception as e:
            top_ratios = f"Error fetching top ratios: {str(e)}"

        try:
            analysis = obj.analysis()
            pros = analysis[0]
            cons = analysis[1]
        except Exception as e:
            pros = f"Error fetching pros: {str(e)}"
            cons = f"Error fetching cons: {str(e)}"

        
        data = {
            "status": status,
            "titles": titles,
            "aboutSection": about_section,
            "topRatios": top_ratios,
            "analysis": {
                "pros": pros,
                "cons": cons
            },
        }

        return JsonResponse(data)

    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)
