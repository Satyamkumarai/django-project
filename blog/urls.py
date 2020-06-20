from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views
#this reprents urls relative to blog/
urlpatterns = [
    path('', PostListView.as_view(),name = 'blog-home'),  #/ is handled by home() in views module
    path('user/<str:username>', UserPostListView.as_view(),name = 'user-posts'),  
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),  #<int:pk> use the primary key of the model with datatype as int 
    path('post/new/',PostCreateView.as_view(),name = 'post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name = 'post-update'),   
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name = 'post-delete'),   
    path('about/',views.about,name = "blog-about"),
]