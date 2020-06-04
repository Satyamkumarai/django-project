"""django_project URL Configuration

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
from django.urls import path,include                                   #need include to include the urls of the apps (here "blog")
from django.contrib.auth import views as auth_views                    #This is where the login and logout views are situated..
from users import views as users_views

from django.conf.urls.static import static                             #This is to serve the static files in dev mode.. 
from django.conf import settings                                       #This is just importing the setting.py

#this is the main urls file 
#this helps to redirct to different apps 
    #  then each app ha it's own urls that redirect to app's views.function() which handles the request.
urlpatterns = [
    #admin_site
    path('admin/', admin.site.urls),  #redirect to urls from urls defined in admin.site.urls 
    
    #home
    path('blog/', include('blog.urls')),  #redirect to blog app using the urls in blog/urls.py
    path("",include("blog.urls")),      # to directly redirect to a app
    
    #register
    path("register/",users_views.register,name = "register"), #adding the registration form
    
    #profile
    path("profile/",users_views.profile,name = "profile"), #adding the registration form


    #login
    #LoginViews is a Class Based view
    #.as_view() to return as a view
    #by default it looks into registration/login.html
    # So we specify the template_name  to our desired path
    path("login/",auth_views.LoginView.as_view(template_name = "users/login.html"),name = "login"), 

    #logout
    path("logout/",auth_views.LogoutView.as_view(template_name = "users/logout.html"),name = "logout" )


]

#this is the way to serve static files in dev mode..only and thus the if block..
if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # document_root is used to specify the root of the media files
