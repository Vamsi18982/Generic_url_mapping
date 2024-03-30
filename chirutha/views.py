from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chirutha(request):
    return render(request,'chirutha.html')
def chirutha_s(request):
    return HttpResponse("this is super hit movie and also first movie")

