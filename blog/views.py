from django.shortcuts import render ,get_object_or_404  

from django.http import HttpResponse  # to send back the response

from .models import Post  # from current dir

# Generic views Class based
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.models import User

# ~~~~Sending Basic Response~~~~~

# def home(request):                      # this is the function that handles the request when routed to url pointed by urls.py
#     return HttpResponse("<h1>Blog HomePage</H1>")
# def about(req):
#     return HttpResponse("""<h1><center>About</center></h1>This is a simple blog post""")

# This is just an example data of what data you may want to use to fill the template
# this could be a result from a daatabase query for example
# posts = [

#     {

#         'author': 'CoreyMS',

#         'title': 'Blog Post 1',

#         'content': 'First post content',

#         'date_posted': 'August 27, 2018'

#     },

#     {

#         'author': 'Jane Doe',

#         'title': 'Blog Post 2',

#         'content': 'Second post content',

#         'date_posted': 'August 28, 2018'

#     }
# ]


# ~~~~~ using Templates~~~~

# def home(request):
#     return render(request,"blog/home.html")  #render the template defined in templates/blog/home.html and then return that as the response
# def about(req):
#     return render(req,"blog/about.html")


# ~~~~~PAssing Data to templates ~~~~

# def home(request):
#     context = {"posts":posts}
#     return render(request,"blog/home.html",context)  #this will pass the context to the template and all it's content will be acessible in the template
# def about(req):
#     return render(req,"blog/about.html",{"title":"About"})  #passing in title


# ~~~~~Querying from DB~~~~~~




#-------------------------------------------------------------------------
def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)                               # this will pass the context to the template and all it's content will be acessible in the template
#-------------------------------------------------------------------------

#--------------------CLASS - BASED  -  VIEWS------------------------------

# class based view For listing the posts on the homepage
#-------------------------------------------------------------------------
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"                                                ##What model that   we need to query
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5 
#-------------------------------------------------------------------------




#this will be used to view the  posts filteresd by users.
#-------------------------------------------------------------------------
class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"                                          ##What model that   we need to query
    context_object_name = "posts"
    paginate_by = 5 

    def get_queryset(self):                                                         #we are overriding this method so that we can return our own queryset
        user =  get_object_or_404( User , username= self.kwargs.get('username'))
        return  Post.objects.filter(author = user).order_by('-date_posted')
#-------------------------------------------------------------------------




# class based view to display each post
#-------------------------------------------------------------------------
class PostDetailView(DetailView):
    model = Post
#-------------------------------------------------------------------------





# class based view to create new post
#-------------------------------------------------------------------------
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title","content",]                                                    # We'll be editing the following fields while creating the model

    def form_valid(self, form):
        form.instance.author = self.request.user                                     # add the author as this user
        return super().form_valid(form)                                              # validate the form
#-------------------------------------------------------------------------




# class to update existing posts
#-------------------------------------------------------------------------
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Post
    fields = ["title","content",]                                                   # we'll be editing the following fields while creating the model

    def form_valid(self, form):
        form.instance.author = self.request.user                                    # add the author as this user
        return super().form_valid(form)                                             # validate the form
    
    def test_func(self):
        post =  self.get_object()
        return  self.request.user == post.author
#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post 
    success_url = '/'
    def test_func(self):
        post =  self.get_object()
        return  self.request.user == post.author
#-------------------------------------------------------------------------



#-------------------------------------------------------------------------
def about(req):
    return render(req, "blog/about.html", {"title": "About"})  # passing in title
#-------------------------------------------------------------------------
