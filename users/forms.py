from django import forms                                 # This is to specify the type of form fields
from django.contrib.auth.models import User              # this is the model that our form will interact with
from django.contrib.auth.forms import UserCreationForm   #this is what our from will inherit
from .models import Profile                              # We need this to update the Profile model..

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()                                          #adding fields is just adding variables
    
    ##This is the meta class 
    #It gives a nested namespace for the configurations
    #It keeps the configurations in one place
    class Meta:                     
        model = User                                                    #The model that will be affected 
        fields = ['username','email','password1','password2']           #The fields that will be passed to the template..either fields or exclude is important


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()                                          #adding additional fields is just adding variables
    
    ##This is the meta class 
    #It gives a nested namespace for the configurations
    #It keeps the configurations in one place
    class Meta:                     
        model = User                                                    #The User model  will be affected 
        fields = ['username','email']                                   #Use these Field from the model..

class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Profile                                                  #This Profile model will be affected
        fields = ['image']