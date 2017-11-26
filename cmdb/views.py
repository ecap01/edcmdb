from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi, You are in the cmdb index")
