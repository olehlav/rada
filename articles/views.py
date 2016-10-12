from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def articles_list_view(request):
	return HttpResponse('<h1>Hello</h1>')