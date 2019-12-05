from django .urls import path 
from .group import view 
app_name ='sp'
urlpatterns =[path ('group/action/',view .action ,name ='action'),path ('offline/active/',view .offline_active ,name ='offline_active'),]
def init ():
    from django .conf import settings 
    from django .conf .urls import url 
    from django .urls import include 
    from simplepro import urls as sp_urls 
    O0OO0OOO0O00OOO0O =__import__ (settings .ROOT_URLCONF ).urls 
    O0OO0OOO0O00OOO0O .urlpatterns .append (url (r'^{}/'.format (sp_urls .app_name ),include ('simplepro.urls',namespace =sp_urls .app_name )),)
