# Django-project
Useful Docs:
    * formating dates:   https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#date
    * CoreyMSchafer Video Playlist: https://www.youtube.com/watch?v=aHC3uTkT9r8&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1

Note For using this file:
    1. $var indicates that var is a variable 
    2. all the code is enclosed in `` or ``` ``` tacs

-------------Creating the django project------------------

1. create Project ->#created the project using: `django startproject <project-name>`

2. run server-># ran the server using: `py manage.py runserver`

3. create app -> #created an app called "blog" using `python manage startapp <app-name>`

<blog/views.py> ->creating the actual views (basic)
    1. importing `HttpResponse` from `django.http` -->to send the httpResponse
    2. created a function called home that will return the httpResponse
    3. Now to add the route this will be managed by the blog/urls.py 


# created <blog/urls.py>   -->this is where we will manage the urls within that app

in <blog/urls.py>
    1. imported `path` from `django.urls`
    2.  imported the `views` in to this file
    3. added a new $urlpatterns list with 1st element as path("",views.home,name = "blog-home")

Now to specify which urls will route to our app "blog" 
This is done in the main urls file..
in <urls.py>
    1. imported `include` from `django.urls`
    2. added path("blog/",include("blog.urls"))  #when the url countains blog/ use the urls defined in blog/urls.py to further 
            route to the correct dest..

in<blog/urls.py and blog/view.py>
    1. added the about option.


Creating Admin/Users:
    first need to create a database for the project
    (more in database migrations )
    `py manage.py makemigrations`  -> detects changes and prepares django to update the database
    `py manage.py migrate`  ->creates the migrations?
    `py manage.py createsuperuser` ->creates the superuser (prompts)
    then you can go to the login page for the admin page



-----------Now Learning to use templates -------------------
1. Create a dir called "Template" in the "blog" dir

Creating the files that will be used as templates
    in <templates/>  
        1. create a subdirectory with same name as the app here "blog"  (overview ) blog -> templates -> blog
        in <templates/blog/>
            1. created "home.html" and "about.html"

Including the App Config
    Our Apps configurations are located in the `apps.py` file
    To use these configurations we must include this in the "apps definitions"
    To add the path to the appconfig class BlogConfig in "settings.py"
        in <setting.py>
            1. append `'blog.apps.BlogConfig'` in the $INSTALLED_APPS varible
            Here blog->appname ,apps -> "apps.py" ,BlogConfig ->class Name within "apps.py"

rendering Templates 
    Now To render the templates in `views` from "blog/templates/<templatefile>"
    in <blog/views>
        1. redefine `home` function to return `render(request,"path-to-templatefile",< Any additional data to be used(See sending data in templates) >)
        2. similarly redefine the `about`

Passing Data to templated to be Rendered
    Now Suppose you have a data (see an example below)
    To pass it in the template just pass it as a dict into `render()`
    in <blog/views>
        1. create $context :dict with a key `"posts"` and value `data`
        2. pass the $context in render() funtion

    Extacting Template Data
        
        int <blog/template/blog/home.html,blog/template/blog/about.html>
            1. use for loops and if statements to write data to the template..

Template Inheritance:
    Instead of repeating code in templates just use template inheritance to make life easier    
    in <blog/template/blog>
        1. Create a "base.html" file 
        
        in <./base.html>
            1. create the basic structure of the html
            2. add a `block` (see rules) to the body section (this block will be over written by child Templates)
        
        in <./home.html>
            1. get rid of all code which is same as that of the "base.html"
            2. At the top declare the template as child template(see rules or see Note on Template inheritance)
            3. create the block to overwrite it and then overwrite it


Adding BootStrap (It's a HTML javascript CSS framework) Loading Static filess
    Download the basic template from bootstrap docs page
    Note Static files like js and css are stored in "static" dir
        1. in <blog/static/main.css>
            1. pasted from https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Django_Blog/03-Templates/django_project/blog/static/blog/main.css
        2. in <blog/template/base.html>
            1. load the static file (see rules) {% load static %} followed by 
            2. `{% static 'blog/main.css' %}` to import the statics 

A Note on Template Inheritance:
        We have something called a block 
        A block can be overwritten by child templates  
        We can have many nested block 
            1. To inherit the contents of a base.html declare   
                a. ` {% extends "path-baseHtmlFile-relative-to-template-path"%} ` at top
                b. create the actual block that you'll be overwriting..
            2. To show which part of the base.html will be used by chid templates to write their Data 
                a. declare a block  ` {% block <blockName> %}
                                        #block content 
                                      {% endblock %} `
            

Note on Database :
    1. ORM object relational Mapper
    2. using sqllite for development
    3. using postgressql for production?
    4. The database stucture can be represented as classes and these are called Models (so that's why we have model.py)
    5. Migrations are a way to restucture your database evenafter it has data in it without messing with the existing data
    6. Querying the database is also like interating with objects

Creating a database: 
    We're going to create a model named "Post"
    To do this:
        <in blog/models.py>
            1. create a new Class named "Post" that inherits from model class 
            The members of this class will represent the fields
            2. Create a $title and set it to  `models.CharField(max_length=100)`
            3. Create a $content and set it to `models.textField()`
            
            Now Import `from django.utils import timezone`
            timezone.now() is a function that gives the current datetime
            
            4. Create a $date_posted and set it to `models.DateTimeField(default = timezone.now)` 
                - Notice that we just passed the function(timezone.now) as the argument 
            
            We Also need the author for the post who will be the user himself/herself
            For that `from django.contrib.auth.models import User`
            Now The author and the post have a one_to_many relationship (one author can have many post but a post can only have one user)
            So we'll set the author to be a ForeignKey (remember a foriegn key is a primary key in another entity that is being refrenced in the current entity)
            
            5. create a $author and set it to `models.ForeignKey(User,on_delete = models.CASCADE)` 
            
            Now To create the migrations just type `py manage.py makemigrations`
            This will create and show the dir where the migrations was made here it will be "blog/migrations/0001_initial.py" file 

            6. Creating __str__(self) method to Print some proper info when querying

        To View the Sql Code:
            `py manage.py <appname> <migrationNumber>`
            IN OUR CASE : `py manage.py blog 0001`
        
        Now that we have created the database We must apply our migrations 
        
        To Apply Our migrations:
            `py migrate.py migrate`
Database Querying:
    ``` from blog.models import Post                                                                    # importing the Post Table
        from django.contrib.auth.models import User                                                     #importing the User Table
        firstUser = User.objects.get(id=1)                                                              #get(<attribute-name> = <attribute-val>)  -> querySet[]
        alsoFirstUser = User.objects.first()                                                            #Returns the first User
        AllPosts = Post.objects.all()                                                                   #returns all the objects in the query set
        post_1 = Post(title="Blog 1",content = "The content of Blog 1",author = User.objects.first())   #creating a post
        post_1.save()                                                                                   #Saving the post
        ```


Fetching the data from the DB:
    <in blog/views.py>
        1. add `from .models import Post`   
        2. in the $context with key "posts" set it to Post.objects.all()
    Formatting the dates:
        <in blog/views.py>
            1.find {{date_posted}} and change it to `{{date_posted|date:"D d M Y"}}`
            Docs : https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#date


Creating a User Registration form:
Using a new app names "users"

    1. py manage.py startapp users

    2. <in settings.py>:
            register our users app by adding `'users.apps.UserConfig'` to $INSTALLED_APPS

    Django has  a users creation form in the form of a class

    3. <in users/views.py>
        1. add `from django.contrib.auth.forms import UserCreationForm`
        2. Add the register function that will handle the register request..
        in register function
            1. set `form = UserCreationForm`
            2. `return render(req,"users/register.html",{"form":form})`

        

    Now TO create the template for Registration..

    <in "users/template/users/register.html">
        1.  inherit from the "blog/base.html" using `{% extends "blog/base.html" %}`
        2.  create the block content.
            1. within the block content Create a div with `class = "content-section"`
                1. within the div create a `form` tag.. with `method="POST"`
                
                    we need to add a csrf_tokens cross-site-forgery-token for added security this is *required
                    1. csrf_token : `{% csrf_token %}

                    To group related elements we add a `fieldset` tag..

                    2. <fieldset class = "form-group"  

                        And a Legend to the form with a `border-bottom mb-4` bootstrap class

                        1. `<legend class = "border-bottom mb-4`>Join Today</legend>` 

                        Now the form.

                        2. `{{ form.as_p }}` to add the contents of the entire form in paragrah tag
                    
                    Now need to add the submit button.. 
                    This will be in a `div` with the `class="from-group"`
                    
                    3. `<div class = "form-group"> `
                        Now The Button.. with `type= "submit"` and bootstrap `class = "btn btn-outline-info"`

                        `<button class = "btn btn-outline-info" type = "submit" >Sign Up</button>
            2. Create a signin message using
                1. a `div` with bootstrap `class = "border-top pt3"`
                    1. within it a  `small` tag.. with `class="text-muted`  -> "Already have an account?"
                    2. along with `a` tag `<a href =  "ml-2" href = "#"> Sign In</a>

    Now To add the Urls But directly to the project 
        <in urls.py>
            1. in $urlpatterns add `path("register/",users_views.register,name= "register")` #basically url:"register/" Req Handled by: users.views.register Name = "register"

    Now to enable our register method to  validate the enter data and redirect if it is correct
        So when the user submits the data ..  byt default the POST is done to the same url..
        So we have request.method = 'POST'
        `request.post` contains the posted data..
        this is passed to a new user creation form
        This `$form` object has a method `is_valid()` that checks the form for errors
        <in users/views.py>
            1. `from django.shortcuts import redirect`
            2. `from django.contrib import messages`  #remember to see how to enable the template to display the messages
            3. ```
                if request.method == "POST":
                    form  = UserCreationForm(request.POST)  # create a from with the post data
                    if form.is_valid():
                        from.save()   # create the user if valid user
                        username = form.cleaned_data["username"] # if the form is valid get username to show message
                        messages.success(request,f'Created Account for {username}')   # show a flash message 
                        return redirect("blog-home")   #redirect to homepage
                else: #get request
                    form = UserCreationForm()
                return render(request,"users/register.html",{"form":form})
               ```

    Now to enable the template (in the base template) to display messages: 
        <in blog/temlate/blog/base.html>
            
            we'll add this just above the content block..

            bootstrap has a alert class `class = "alert alert-<alert-type>"
            The $message in each $messages  has a `.tag` that specifies the type of the message passed
            So we make a `div` with `class = "alert alert-{{ message.tag }}
            then the actual message content within the div
            ```
                <!-- See if the template recieved any messages.. -->
                {% if messages %}  
                    <!-- Loop Through the messages -->

                    {% for message in messages %}
                        <div class="alert alert-{{ message.tag }}">
                            {{ message }}
                        </div>
                    {% endfor %}


                {% endif %}
            ```
            
    Now  TO BE able to change the contents of the default `user creation form` that django provides we have to create a new class
        1. Create `users/forms.py`
        <in users/froms.py>
            1.  ```
                    from django import forms                                                # This is to specify the type of form fields
                    from django.contrib.auth.models import User                             # this is the model that our form will interact with
                    from django.contrib.auth.forms import UserCreationForm                  #this is what our from will inherit

                    class UserRegistrationForm(UserCreationForm):
                        email = forms.EmailField()                                          #adding fields is just adding variables

                        ##This is the meta class 
                        #It gives a nested namespace for the configurations
                        #It keeps the configurations in one place
                        class Meta:                     
                            model = User                                                    #The model that will be affected 
                            fields = ['username','email','password1','password2']           #The fields and their orders
                ```
        Now to use our registration form instead of UserCreationForm
        <in users/views.py>
            1. delete the `from django.contrib.auth.forms import UserCreationForm
            2. add `from .forms import UserRegistrationForm`
            3. replace all UserCreationForm with UserRegistrationForm
            
    Making our forms "Crispy":
        1. `pip install django-crispy-forms`
        
        <in setting.py>
            1. add to $INSTALLED_APPS `crispy_forms`
            2. At the end add `$CRISPY_TEMPLATE_PACK = 'bootstrap4'`
        
        Now to be able to use the crispy froms tags and filters we must load it first
        <in users/temlates/users/register.html>
            1. add `{% load crispy_forms_tags %}`
            2. replace  `{{forms.as_p}}`  with `{{ forms|crispy }}`

    Adding the login and Logout funtionality
        Since the views are  Already provided by django we directly add these in the `urls.py`
        <in urls.py>
            1. add `from django.contrib.auth import views as auth_views

            The auth_views contains the `LoginView` and the `LogoutView` as classes 
            The `as_view()` method is used to return a view..
            By default the login and the logout views that django provides look in the `registration/<template-name>.html`
            But by specifying the `template_name` in the `as_view()` method we can change it..
            ```
                path("login/",auth_views.LoginView.as_view(template_name = "users/login.html"),name = "login"), 
                path("logout/",auth_views.LogoutView.as_view(template_name = "users/logout.html"),name = "logout" )
            ```
        Templates For Login :
            1. create a new "users/template/users/login.html" file 
            
            <in "users/template/users/login.html">
                1. copy the template from the "users/template/users/register.html"
                2. replace `Sign Up!` button name with `Login`
                3. "Need and account to register"
                4. add the login `href = "{% url 'login' %}"` (Do the same in the register.html if you haven't)

            Now after login it redirects to /Accounts/profile To change that 
            
            <in setting.py>
                at the end add $LOGIN_REDIRECT_URL = "blog-home"

            Now after the user registers we want them to be redirected to the login page 

            <in users/views>
            
                1. in the register function change the message to `messages.success(request,f"Your account has been created You cannow Login!")`
                2. change redirect to `login`
            
            Now to add contents to logout.html
            <in users/template/users/logout.html>
                1. Add this:
                    ```
                    {% extends "blog/base.html" %}
                    {% block content %}
                        <h2 >You Have Been Logged Out</h2>
                        <div class="border-top pt-3">
                            <small class="text-muted">
                                <a href="{% url 'login' %}" >Log in again</a>
                            </small>
                        </div>
                    {% endblock content %}
                    ```
            Now Making the side navigation bar working..
                <in blog/template/blog/base.html>
                    1. add the hrefs to `{% url 'login' %}` and `{% url 'register' %}` for login and register text
                    
                    If the user is logged in the `user` object is available in the template with `user.is_authenticated` set to `True`

                    2. add a conditional if and else: 
                        ```
                        {% if user.is_authenticated %}
                        <a class="nav-item nav-link" href="{% url 'logout' %}">Logout</a>
                        {% else %}
                        <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
                        <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
                        {% endif %}

                        ```
            Now to add the profiles page:
                
                Adding Url path
                <in urls.py>

                    1. add `path("profile/",users_views.profile,name = "profile"), #adding the registration form`

                Adding the views
                <in users/views.py>
                    1. import the `from django.contrib.auth.decorators import login_required`decorator

                    2. add the  the function `profile` decorated with the decorator 

                    3. in the function body `return render(request,"users/profile.html")`
                
                Adding the template:
                    Now create a  file "users/template/users/profile.html"
                        1. add the necesary lines of code..
                            Note : If the user is logged in  the `{{ user }}` can be used to get the details
                            for Now just add the base template inheritance line  {% extends "blog/base.html %}
                            and the `<h2> {{ user.username }}</h2>`

                Now by default  the login url for django is "accounts/login"  to change this:
                    <in settings.py>
                        1. add $LOGIN_URL and set is to  `'login'`
    Enabling the user to edit their profiles:

        



///An example for data
posts = [

    {

        'author': 'CoreyMS',

        'title': 'Blog Post 1',

        'content': 'First post content',

        'date_posted': 'August 27, 2018'

    },

    {

        'author': 'Jane Doe',

        'title': 'Blog Post 2',

        'content': 'Second post content',

        'date_posted': 'August 28, 2018'

    }
]

//Rules for working with Templates
    Rules:
            1. for Loops:   {%for var in vars%}
                                #body of the for loop
                            {%endfor%} 
            2. varibles:   {{varName}}

            3. Block:       {% block <blockName> %}
                                #block content 
                            {% endblock %}
            4. Template inheritance : {% extends "path-baseHtmlFile-relative-to-template-path"%} 
                            Note: Should be declared at the top of the child template
            5. Loading Static file :
                                    1. `{% load static %}`   # to load the static file 
                                    2. `href = {% static '<appname>/<staticfileName>'%}`  #to include the static file 


Dabase Related Commands:
    1. running shell : `py manage.py shell`
    2. Querying:
            1. importing the users :                `from django.contrib.auth.models import User`
            2. importing Our Own Entities:          `from <appname>.models import <entity-name>
            3. First entry in an entity:            `<entity-name>.objects.first()`                             #similarly last
            4. All entries:                         `<entity-name>.objects.all()`                               #returns a querySet    
            5. adding new Entity:                   `<entity-name>(<attributes = "<values>").save()`            Creates a new entry in the <entity-name> table
            6. Get:                                 `<entity-name>.objects.get(<attrib> = "<value>")
            7. Filter                               `<entity-name>.objects.filter(<attrib= "<value>")           #search by attrib ->queryset
            8. Getting data of oneobject from another object of another (related)entity
                    all posts of User:              `<user-object>.post_set.all()`
                    create:                         `<user-object>.<related-entity-name>_set.create(attribs)`    
            
Directory Structure :
    C:.
    â”œâ”€â”€â”€.vscode                                                         #vscode config
    â”‚
    â””â”€â”€â”€django_project                                                  #main project dir 
        â”‚   db.sqlite3
        â”‚   manage.py                                                       #this is what manages the enire project
        â”‚
        â”œâ”€â”€â”€blog                                                        #The apps folder    
        â”‚   â”‚   admin.py                                                     #this is where we register our models that our admin can change using the GUI
        â”‚   â”‚   apps.py                                                      #The apps configurations file 
        â”‚   â”‚   models.py                                                    #This is where we create our entities
        â”‚   â”‚   tests.py                                                     
        â”‚   â”‚   urls.py                                                      #The urls within the app are defined here 
        â”‚   â”‚   views.py                                                     #This is where we render our templates
        â”‚   â”‚   __init__.py 
        â”‚   â”‚
        â”‚   â”œâ”€â”€â”€migrations
        â”‚   â”‚       __init__.py
        â”‚   â”‚
        â”‚   â”œâ”€â”€â”€static                                                   #The Static folder(For Js and Css)
        â”‚   â”‚   â””â”€â”€â”€blog                                                    #The App name
        â”‚   â”‚           main.css                                                #The Css file for the app
        â”‚   â”‚
        â”‚   â”œâ”€â”€â”€templates                                                #Templates Folder To store the templates
        â”‚       â””â”€â”€â”€blog                                                    #The appname
        â”‚               about.html                                              #about.html for the "blog" app
        â”‚               base.html                                               #Base Template for "blog" app
        â”‚               home.html                                               #home.html for "blog" app
        â”‚   
        â””â”€â”€â”€django_project                                                      #This is the folder where the project-wide settings are located
                asgi.py 
                settings.py                                                         #settings for the entire project
                urls.py                                                             #project urls redirects
                wsgi.py                                                             #file to configure the wsgi server
                __init__.py
             
