from django.shortcuts import render

# Create your views here.
# _____________________________________________________________________________________________________________
# from django.http import HttpResponse
# def learn_django(request):
# 	coursename={'cname':'django'}
# 	return render(request, 'course/courseone.html', 
# 	context=coursename)

def learn_django(request):
	cname:'django'
	duration= '4 months'
	seats = 10
	django_details = {'nm':cname, 'du':duration, 'st':seats}
	return render(request, 'course/courseone.html', 
	django_details)


def learn_python(request):
    return render(request, 'course/coursetwo.html', {'cname':'django learn python'})
