# from django.test import LiveServerTestCase, TestCase

# # Create your tests here.

# from django.shortcuts import render, HttpResponse
# from datetime import datetime
# from scrapAPP.models import User

# from .views import index



# import os
# # import linkedin.constants as const
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # from .result import Result
# # from selenium.webdriver.remote.webelement import WebElement





# class Linkedin(webdriver.Chrome):


   
#     def __init__(self, executable_path=r"C:/SeleniumDriver",  teardown=False ):
       
#     #    self.items = self.pull_divs()
#     #    self.result_element=self.pull_items()
        

#        self.executable_path = executable_path
#        self.teardown = teardown
#        os.environ['PATH'] += self.executable_path
#        options = webdriver.ChromeOptions()
#        options.add_experimental_option('excludeSwitches', ['enable-logging'])

#        super(Linkedin, self).__init__(options=options)
#        self.implicitly_wait(15)


#     def __exit__(self, *args):
#         if self.teardown:

#          self.quit()   

#     def linkedin_page(self,request):
       
#         link = index()
#         print(link)
                
#         self.get(link) 


#     def signup(self, ):
#         clickonsign_in= self.find_element_by_class_name(
#             "main__sign-in-link"
#         ) 
#         clickonsign_in.click()
    
    
#     def signin(self,email, pasw)  :
#         email_input=self.find_element_by_id("username")
#         email_input.clear()
#         email_input.send_keys(email)
#         pasw_input=self.find_element_by_id("password")
#         pasw_input.clear()
#         pasw_input.send_keys(pasw)
        
#         sign_click=self.find_element_by_css_selector('button[class="btn__primary--large from__button--floating"]')
#         sign_click.click()



#     # def pull_divs(self):
#     #     return self.result_element.find_element_by_class_name("entity-result__item")  
    


#     def pull_titles(self):
  
#         element= self.find_elements(By.CSS_SELECTOR, "span.entity-result__title-text")
#         for e in element:
#          print(e.get_attribute('innerText'))

#     def pull_subtitles(self):
  
#         element= self.find_elements(By.CSS_SELECTOR, "div.entity-result__primary-subtitle ")
#         for e in element:
#          print(e.get_attribute('innerText'))
   
    

#     def pull_locations(self):
  
#         element= self.find_elements(By.CSS_SELECTOR, "div.entity-result__primary-subtitle ")
#         for e in element:
#          print(e.get_attribute('innerText'))


#     def pull_links(self):
  
#         element= self.find_elements(By.CSS_SELECTOR, "a.app-aware-link")
#         # element= self.find_elements(By.CSS_SELECTOR, "span.entity-result__title-text.href")
        
#         for e in element:
#          print(e.get_attribute('href'))
#         #  print(e)     

#     # def result(self):
#     #     entry_result = self.find_element_by_class_name('entity-result__item"') entity-result__title-text 


#         # report = Result()
#         # report.pull_items()
        
# with Linkedin() as Lbot:
#     Lbot.linkedin_page()
#     Lbot.signup()
#     Lbot.signin(email="kumaranish10092000@gmail.com",pasw="Akm911@linkedin")
#     # Lbot.refresh()
#     Lbot.pull_titles()
#     Lbot.pull_subtitles()
#     Lbot.pull_locations()
#     Lbot.pull_links()
        
# class LinkedinTest(LiveServerTestCase):
#     test = Linkedin()
#     # pass










