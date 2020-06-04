from django.db import models
from django.contrib.auth.models import User
#Extending the user model User model to be able to additional info

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)                              ##Creting a one to one relationship to the User
    image = models.ImageField(default = "default.jpg",upload_to = 'profile_pics')           ##An Image field with default = default.jpg and upload_to = <folderName>


    def __str__(self):
        return f'{self.user.username} Profile'
