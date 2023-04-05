"""Gases URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from Gases.views import homehtml, fallas, triangulo1
from Gases.views import triangulo4, triangulo5, TransfList, TransfList1
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('triangulo_app.urls')),
    path('', homehtml),
    path('fallas/', fallas),
    path('fallas/triangulo1/<int:id>', triangulo1),
    path('fallas/triangulo4/<int:id>', triangulo4),
    path('fallas/triangulo5/<int:id>', triangulo5),
    path('login', LoginView.as_view(template_name = 'login.html')),
    path('logout', LogoutView.as_view(template_name = 'logout.html')),
    path('api/buscar/', TransfList.as_view()),
    path('api/mostrar/', TransfList1.as_view())
]
