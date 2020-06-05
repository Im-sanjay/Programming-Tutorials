from django.shortcuts import render

# Create your views here.

def learn_django(request):
	return render(request, 'course/courseinfo.html')


def course_detail(request):
	return render(request, 'course/coursedetail.html')
