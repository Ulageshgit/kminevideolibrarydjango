"""registration URL Configuration

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
from kmineapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('Bootstrapvideos',views.page1,name='page1'),
    path('contactt',views.page2,name='page2'),
    path('CSSvideos',views.page3,name='page3'),
    path('Database',views.page4,name='page4'),
    path('Dsuvideos',views.page5,name='page5'),
    path('Gitvideos',views.page6,name='page6'),
    path('Htmlvideos',views.page7,name='page7'),
    path('Linuxvideos',views.page8,name='page8'),
    path('Python',views.page9,name='page9'),
    path('Photoshop',views.page10,name='page10'),
    path('Reactjs',views.page11,name='page11'),
    path('contactt',views.contact,name='contact'),
    path('login/',views.LoginPage,name='login'),
    path('index/',views.index,name='index'),
    path('logout/',views.LogoutPage,name='logout'),


    
]
