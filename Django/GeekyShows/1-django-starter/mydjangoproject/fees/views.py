from django.shortcuts import render

# Create your views here.

# _____________________________________________________________________________________________________________
from django.http import HttpResponse
def fees_django(request):
    return render(request, 'fees/feesone.html')

def fees_python(request):
    return render(request, 'fees/feestwo.html')