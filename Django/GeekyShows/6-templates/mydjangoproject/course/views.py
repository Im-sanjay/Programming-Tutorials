from django.shortcuts import render

# Create your views here.
# _____________________________________________________________________________________________________________
from django.http import HttpResponse
def learn_django(request):
    return render(request, 'courseone.html')

def learn_python(request):
    return render(request, 'coursetwo.html')
