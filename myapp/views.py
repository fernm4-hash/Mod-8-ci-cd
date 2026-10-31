from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1>")

def api_hello(request):
    return JsonResponse({"message": "Hello, API!", "course": "CSC 325"})
    