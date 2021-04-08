#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homePageView(request):
	return HttpResponse('hello, this is ISHA from T4 Batch and my PRN is 1942204')