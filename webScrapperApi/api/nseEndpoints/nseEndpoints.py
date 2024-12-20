from django.http.response import JsonResponse
from api.nseEndpoints import nse as n



def Getdata(request):
    company_name = request.GET.get('companyName')
    if not company_name:
        return JsonResponse({"error": "companyName parameter is required"}, status=400)

    try:
        obj = n.NSE(company_name)
        status = obj.getStatus()
        if status != 200:
            return JsonResponse({"message": "Company not found, please check."}, status=404)
        
        try:
            data = obj.getData()
            data = {
            'status':status,
            'data': "data"
            }
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=401)
        

    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)