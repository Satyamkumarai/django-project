from django.shortcuts import render,redirect #redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages  # to create the flash messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm

# def register(request):                                              #this will handle the request..
#     form = UserCreationForm()                                       #create a form..
#     return render(request,"users/register.html",{"form":form})      #render users/register.html and pass that form data..

#handling the posted data..
def register(request):
    #the request has a method which tells what type of request it was 
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned _data.get("username")           # a dict with data of the from..
            messages.success(request,f"Your account has been created You cannow Login!")
            #then redirect to login_page..
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,"users/register.html",{"form":form})



#this is a decorator to ensure that this function only gets called if the user has already logged in
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user) #
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Your account has been Updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user) #
        p_form = ProfileUpdateForm(instance=  request.user.profile)
    context = {                                                          #creating the context dict to pass in values to the template..
        'u_form':u_form,
        'p_form':p_form

    }
    return render(request,"users/profile.html",context)




"""
types og message
messages
    .debug
    .info
    .success
    .warning
    .error


"""