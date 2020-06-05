from django.shortcuts import render

# Create your views here.

# _____________________________________________________________________________________________________________
from django.http import HttpResponse
def fees_django(request):
    return HttpResponse('200 from fees application ')

def fees_python(request):
    return HttpResponse('400 from fees application')