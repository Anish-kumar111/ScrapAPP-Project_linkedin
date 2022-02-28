from django.contrib import admin
from django.urls import path
from scrapAPP import views

urlpatterns = [

    path("", views.index, name='home'),
        path("about", views.about, name='about'),
            path("register", views.register, name='register'),
         path("contact", views.contact, name='contact'),       
               

    
]
# path("", TemplateView.as_view(template_name="index.html")),