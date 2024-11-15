from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. 
def res(request):
  html = "<h1>Hello World</h1>"
  return HttpResponse(html)
def res2(request):
  return HttpResponse("i love you")
