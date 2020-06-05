from django.shortcuts import render

# Create your views here.
# _____________________________________________________________________________________________________________
from django.http import HttpResponse
def learn_django(request):
    return HttpResponse('Hello Django , from course application')

def learn_python(request):
    return HttpResponse('Hello Python, from course application')
