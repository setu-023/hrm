from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def homePage(request):

    return JsonResponse({'say':'hello world'})
