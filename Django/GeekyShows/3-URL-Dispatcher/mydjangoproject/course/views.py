from django.shortcuts import render

# Create your views here.
# _____________________________________________________________________________________________________________
from django.http import HttpResponse
def learn_django(request):
    return HttpResponse('HELLO DJANGO')
