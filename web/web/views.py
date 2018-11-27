from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def json(request):
    return JsonResponse({'test': 'test'})