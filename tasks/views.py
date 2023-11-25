from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def seederAPI(request):
  if request.method=='POST':
    return JsonResponse({"message": "Seeders generados correctamente"}, safe=False)
    
