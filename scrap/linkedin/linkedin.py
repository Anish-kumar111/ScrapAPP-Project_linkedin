

import os , csv

from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
import os

import pandas as pd


os.environ['PATH'] = r"/"




class Linkedin(webdriver.Chrome):
    # def __init__(self,  teardown=False ):
    def __init__(self, executable_path="/",  teardown=False ):
       
    #    self.items = self.pull_divs()
    #    self.result_element=self.pull_items()
        
    #    self.delete_all_cookies
       self.executable_path = executable_path
       self.teardown = teardown
    #    self.maximize_window()
    #    os.environ['PATH'] += self.executable_path
       options = webdriver.ChromeOptions()
       options.add_experimental_option('excludeSwitches', ['enable-logging'])

       super(Linkedin, self).__init__(options=options)
       self.implicitly_wait(30)


    def __exit__(self, *args):
        if self.teardown:

         self.quit()   

    def linkedin_page(self, link):
        self.get(link) 


    def signup(self, ):
        clickonsign_in= self.find_element_by_class_name(
            "main__sign-in-link"
        ) 
        clickonsign_in.click()
    
    
    def signin(self,email, pasw)  :
        email_input=self.find_element_by_id("username")
        email_input.clear()
        email_input.send_keys(email)
        pasw_input=self.find_element_by_id("password")
        pasw_input.clear()
        pasw_input.send_keys(pasw)
        
        sign_click=self.find_element_by_css_selector('button[class="btn__primary--large from__button--floating"]')
        sign_click.click()

 
 
 
    def signupp(self, ):
        clickonsign_in= self.find_element_by_link_text(
            "Already on LinkedIn?"
        ) 
        clickonsign_in.click()

    def signinn(self,email, pasw)  :
        email_input=self.find_element_by_id("session_key")
        email_input.clear()
        email_input.send_keys(email)
        pasw_input=self.find_element_by_id("session_password")
        pasw_input.clear()
        pasw_input.send_keys(pasw)
        
        sign_click=self.find_element_by_css_selector('button[class="sign-in-form__submit-button"]')
        sign_click.click()


    # def pull_divs(self):
    #     return self.result_element.find_element_by_class_name("entity-result__item")  
    

    def openemp_page(self):
        emp_list = self.find_element_by_xpath("//a[@class='face-pile__cta']")
        # emp_list= self.find_element(By.XPATH, "//body/div[5]/div[3]/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[2]/span[1]")
        emp_list.click()
    def openprofile(self):
        emp_list = self.find_element_by_xpath("//a[@class='app-aware-link']")
        # emp_list= self.find_element(By.XPATH, "//body/div[5]/div[3]/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[2]/span[1]")
        emp_list.click()


    def pull_titles(self):


        title_list=[]
        element= self.find_elements(By.CSS_SELECTOR, "span.entity-result__title-text")
        for e in element:
            title_list.append(e.text) 

        
        element= self.find_elements(By.CSS_SELECTOR, "div.entity-result__primary-subtitle ")
       
        bio_list = []
        for e in element:
            
          bio_list.append(e.get_attribute('innerText')) 

                      
        loc_list=[]
        element= self.find_elements(By.CSS_SELECTOR, "div.entity-result__secondary-subtitle ")
        
        
        for e in element:
         loc_list.append(e.get_attribute('innerText'))
                  
        
        links_list=[]
        element= self.find_elements(By.CSS_SELECTOR, "a.app-aware-link")


        for e in element:
         links_list.append(e.get_attribute('href')) 


        templist = zip(title_list,bio_list,loc_list,links_list)
  
        df = pd.DataFrame(templist, columns = ['Name','Bio','Location','Links'])

        print(df)
        df.to_csv("Output.csv")         


    
    



        #   f = open('Output.csv', 'w', newline='')
       
        #   writer = csv.writer(f)
        #   writer.writerows(str(list))
        #   f.close()  
          
                
        #   f.write(str(list))
        #   f.close()
        # Serializing json 
        # json_object = json.dumps(list, indent = 4)
  
        # Writing to sample.json
        # with open("sample.json", "w") as outfile:
        #      outfile.write(json_object)



    def pull_subtitles(self):
  
        element= self.find_elements(By.CSS_SELECTOR, "div.entity-result__primary-subtitle ")
       
        links_list = []
        for e in element:
            
          links_list.append(e.get_attribute('innerText')) 

    

    def pull_locations(self):

        list=[]
        element= self.find_elements(By.CSS_SELECTOR, "div.entity-result__primary-subtitle ")
        for e in element:
         print(e.get_attribute('innerText'))


    def pull_links(self):
        list=[]
        element= self.find_elements(By.CSS_SELECTOR, "a.app-aware-link")
     
        
        for e in element:
         list.append(e.get_attribute('href')) 


        
        #  print(e)     

    # def result(self):
    #     entry_result = self.find_element_by_class_name('entity-result__item"') entity-result__title-text 


        # report = Result()
        # report.pull_items()

    def page_signup(self, ):
        clickonsign_in= self.find_element_by_class_name(
            "authwall-join-form__form-toggle--bottom"
        ) 
        clickonsign_in.click()
    
    
    def page_signin(self,email, pasw)  :
        email_input=self.find_element_by_id("session_key")
        email_input.clear()
        email_input.send_keys(email)
        pasw_input=self.find_element_by_id("session_password")
        pasw_input.clear()
        pasw_input.send_keys(pasw)
        
        sign_click=self.find_element_by_css_selector('button[class="sign-in-form__submit-button"]')
        sign_click.click()
       
    def education(self):
  
        # link= self.find_elements(By.XPATH, "//body/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[4]/div[3]/ul[1]/li[1]/div[1]/div[2]/div[1]/a[1]")
       
        
        # for e in link:
        #  link.append(e.get_attribute('href'))

        # title= self.find_elements(By.XPATH, "//body/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[4]/div[3]/ul[1]/li[1]/div[1]/div[2]/div[1]/a[1]/div[1]/span[1]/span[1]")
       
        
        # for e in title:
        #  title.append(e.get_attribute('innerText'))


        # desc= self.find_elements(By.XPATH, "//body/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[4]/div[3]/ul[1]/li[1]/div[1]/div[2]/div[1]/a[1]/span[1]/span[1]")
       
        
        # for e in desc:
        #  desc.append(e.get_attribute('innerText'))         


        # sess= self.find_elements(By.XPATH, "//body/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[4]/div[3]/ul[1]/li[1]/div[1]/div[2]/div[1]/a[1]/span[2]/span[1]")
        sess = self.find_element_by_xpath("//body/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[4]/div[3]/ul[1]/li[1]/div[1]/div[2]/div[1]/a[1]/span[2]/span[1]").text
        
        for e in sess:
        #  sess.append(e.get_attribute('innerText'))
        #  list= (e.text
         print(e)
        #  data=zip(link,title,desc,sess)
        #  df = pd.DataFrame(data, columns = ['Name','Bio','Location','Links'])

        #  print(df)
        #  df.to_csv("Education.csv")   
        

        





    def experience(self):
  
        # link= self.find_elements(By.XPATH, "//body/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[4]/div[3]/ul[1]/li[1]/div[1]/div[2]/div[1]/a[1]")
       
        
        # for e in link:
        #  print(e.get_attribute('href'))

        title= self.find_elements(By.XPATH, "//body/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[3]/div[3]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]")
       
        
        for e in title:
         print(e.get_attribute('innerText'))

       
       
        sub= self.find_elements(By.XPATH, "//body/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[3]/div[3]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]")
       
        
        for e in sub:
         print(e.get_attribute('innerText'))        


        # sess= self.find_elements(By.XPATH, "//body/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/section[3]/div[3]/ul[1]/li[1]/div[1]/div[2]/div[1]/div[1]/span[2]/span[1]")
       
        
        # for e in sess:
        #  strings = e.get_attribute('innerText')
     
        #  print(strings)

        #  data=zip()
        #  df = pd.DataFrame(data, columns = ['Name','Bio','Location','Links'])

        #  print(df)
        #  df.to_csv("Experience.csv")            

