from django.shortcuts import render

# Create your views here.

# _____________________________________________________________________________________________________________
from django.http import HttpResponse
def fees_django(request):
    return HttpResponse('300')
