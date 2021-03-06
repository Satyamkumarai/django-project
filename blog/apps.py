from django.apps import AppConfig

#this is where the configurations of our app "blog" is located
#To work with this config it must be included into the project "setting.py" under $INSTALLED_APPS
#as blog.apps.BlogConfig <app-name>.apps.<class-name>
class BlogConfig(AppConfig):    
    name = 'blog'
    
    #connecting the signals.. Since we are using the `reciever` decorator we need to import the signals in the ready function of the config..
    def ready(self):
        import users.signals

