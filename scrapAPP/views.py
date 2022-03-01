
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime

import sweetify
from django.contrib import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrap.linkedin.linkedin import Linkedin
# Create your views here.
def index(request):
   
       if request.method == "GET":
        link = request.GET.get('link')
        email = request.GET.get('email')
        password = request.GET.get('password') 
        # messages.success(request, f"form filled")       
        
        try:
            # driver.get(link)
            with Linkedin() as Lbot:
                
                  
                Lbot.linkedin_page(link=link)
                Lbot.openemp_page()
                Lbot.signup()
                Lbot.signin(email=email,pasw=password)
                # Lbot.openprofile()

                # Lbot.page_signup()
                # Lbot.page_signin(email=email,pasw=password)  
                # Lbot.openprofile()
                Lbot.pull_titles()
                
                # Lbot.experience()

                # Lbot.education()
                sweetify.success(request, 'Scraping Done', text='Thanks for choosing us',
                     persistent='Scrap Again')
               
                
               
               
               
                # driver.get(link)   
                # elements = driver.find_elements(By.TAG_NAME, 'h2')

                # for e in elements:
                #  print(e.text)
        except :
        
            
     
               return render(request, 'index.html')
        # return HttpResponse("Scraping Done !")
        # else :
            
             
                             
       return redirect("/")
        





























from scrapAPP.models import User
def about(request):
    return render(request, 'about.html')
def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        register = User(name=name, email=email, desc=desc, date=datetime.today())
        register.save()
        
          
    return render(request, 'register.html')
def contact(request):
    return render(request, 'contact.html')