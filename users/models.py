from django.db import models
from django.contrib.auth.models import User
from PIL import Image                                                                      ##using the pillow lib to manipulate the images..

#Extending the user model User model to be able to additional info

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)                              ##Creting a one to one relationship to the User
    image = models.ImageField(default = "default.jpg",upload_to = 'profile_pics')           ##An Image field with default = default.jpg and upload_to = <folderName>


    def __str__(self):
        return f'{self.user.username} Profile'

    #overriding the save method to resize the images while being saved.
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)
        if img.height>300 or img.width>300:
            outputSize = (300,300)
            img.thumbnail(outputSize)
            img.save(self.image.path)