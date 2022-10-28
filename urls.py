"""new_env URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from http.client import responses
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def rootRouteHandler(request):
    response = HttpResponse("<h1>Welcome to the internet</h1>") # every request must receive one response
    print('=-=-=-=-=-=-=-=')
    print(dir(request))
    print('--------------')
    print(dir(response))
    print('=-=-=-=-=-=-=-=')
    return response


def anotherRouteHandler(request):
    response = HttpResponse("<marquee>We can make as many routes as we want</marquee>")
    response.status_code = 418

    # django automatically puts query string variables into a dictionary
    print(request.GET.get('format'))

    return response 

def withParams(request, format='h1'):
    print(format)
    return HttpResponse(f"<{format}>Hello Django</{format}")

def recArea(request):
    height = int(request.GET.get("height"))
    width = int(request.GET.get("width"))
    response = HttpResponse(f'<h1>Rectangle area: {height*width}</h1>')
    response.status_code= 400
    return response

def circleArea(request,radius):
    return HttpResponse(f'Circle Area: {(radius**2) * 3.14}')
    
    
    

urlpatterns = [
    path('admin/', admin.site.urls), # default admin routes, provided for free by django
    path('', rootRouteHandler),
    path('another-route/', anotherRouteHandler),
    path('another-route/<str:format>', withParams),
    path('rectangle/area/', recArea),
    path('circle/area/<int:radius>',circleArea)
]
