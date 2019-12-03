from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static 
from Django_registration.Django_registration import views

urlpatterns = [

    url(r'^register', views.register,name="register"),
   
    ]