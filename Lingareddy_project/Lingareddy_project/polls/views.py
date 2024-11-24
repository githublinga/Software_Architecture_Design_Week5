from django.shortcuts import render
from django.http import JsonResponse
def index(request):
    #access Model Objects and use templates to prepare responses.
    return JsonResponse({"Message":"Hello World!"})

# Create your views here.
