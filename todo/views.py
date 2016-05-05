from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello world. You're at todo's polls index.")

# Create your views here.
