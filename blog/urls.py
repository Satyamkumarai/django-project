from django.urls import path
from . import views
#this reprents urls relative to blog/
urlpatterns = [
    path('', views.home,name = 'blog-home'),  #/ is handled by home() in views module
    path('about/',views.about,name = "blog-about"),
]