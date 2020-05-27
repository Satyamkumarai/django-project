from django.contrib import admin

from .models import Post  #import the model from the current dir

admin.site.register(Post) #registering the Post objects to the adminsite
