from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static 
from Django_sign_up import views

urlpatterns = [

    url(r'^register', views.register,name="register"),
   
    ]