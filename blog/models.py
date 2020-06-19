from django.db import models
from django.utils import timezone                               #timezone.now function this is for the date_posted field
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):                                       # we have an implicit PK "id "
    title = models.CharField(max_length=100)                    #title is a characterfield of maxlength 100
    content = models.TextField()                                #content is Text Field Who's size is unlimited (almost)
    date_posted = models.DateTimeField(default = timezone.now)  #date_posted is a DateTimeField with current datetime as the default value
    author =  models.ForeignKey(User,on_delete=models.CASCADE)  # author is a FK Mapped to (referencing) User When author(USer) is deleted this model is dropped (Deleted)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail',kwargs = {'pk':self.pk})