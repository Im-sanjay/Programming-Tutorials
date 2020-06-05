"""mydjangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from fees import views as fv
from course import views as cv

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('learn/', views.learn_django), # http://localhost:5000/learn/
    path('course/', cv.learn_django), # http://localhost:5000/course/
    path('', cv.learn_django),  # http://localhost:5000/
    path('fees', fv.fees_django),

]
