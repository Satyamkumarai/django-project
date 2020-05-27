from django.shortcuts import render

from django.http import HttpResponse  #to send back the response

#~~~~Sending Basic Response~~~~~

# def home(request):                      # this is the function that handles the request when routed to url pointed by urls.py
#     return HttpResponse("<h1>Blog HomePage</H1>")
# def about(req):
#     return HttpResponse("""<h1><center>About</center></h1>This is a simple blog post""")

#This is just an example data of what data you may want to use to fill the template
#this could be a result from a daatabase query for example
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




#~~~~~ using Templates~~~~

# def home(request):
#     return render(request,"blog/home.html")  #render the template defined in templates/blog/home.html and then return that as the response
# def about(req):
#     return render(req,"blog/about.html")


#~~~~~PAssing Data to templates ~~~~

# def home(request):
#     context = {"posts":posts}
#     return render(request,"blog/home.html",context)  #this will pass the context to the template and all it's content will be acessible in the template
# def about(req):
#     return render(req,"blog/about.html",{"title":"About"})  #passing in title




#~~~~~Querying from DB~~~~~~


from .models import Post  #from current dir
def home(request):
    context = {"posts":Post.objects.all()}
    return render(request,"blog/home.html",context)  #this will pass the context to the template and all it's content will be acessible in the template
def about(req):
    return render(req,"blog/about.html",{"title":"About"})  #passing in title
