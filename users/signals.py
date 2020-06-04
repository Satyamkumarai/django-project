from django.db.models.signals import post_save  # post_save is a signal that is called after a model.save() is called...
from django.dispatch import receiver            #This is the reciever that will catch the signal?
from django.contrib.auth.models import User     #The user
from .models import Profile                     #The Profile


#This is just connecting the signal to the reciever using the reciever decorator ..
#another way would be <signal>.connect(<callbackfunction>)
@receiver(post_save,sender=User)                                    #We are connecting the post_save signal to Sender ->User
def create_profile(sender,instance ,created,**kwargs):              #When the signal is fired ,the create_profile method is invoked..
    if created :
        Profile.objects.create(user = instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()