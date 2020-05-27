from django.apps import AppConfig

#this is where the configurations of our app "blog" is located
#To work with this config it must be included into the project "setting.py" under $INSTALLED_APPS
#as blog.apps.BlogConfig <app-name>.apps.<class-name>
class BlogConfig(AppConfig):    
    name = 'blog'
