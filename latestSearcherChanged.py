# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from traceback import print_exc
import time
PATH= "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
URL='https://indeed.com'

print(driver.title) # get webpage title

class jobSearch:
    def __init__(self):
        driver.get(URL) 
    def signIn(self):
        
        ################# Go to sign in page
        xpath="//div[@data-gnav-element-name='SignIn']/a"
        search = driver.find_element_by_xpath(xpath)
        date_URL=search.get_attribute('href')
        
        
        driver.get(date_URL) 
        ################# Sign in 
        # Input username
        search=driver.find_element_by_id('login-email-input')
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(Keys.DELETE)
        search.send_keys(USER_EMAIL)
        # Input password
        search=driver.find_element_by_id('login-password-input')
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(Keys.DELETE)
        search.send_keys(USER_PASS)
        # Hit submit
        submit=driver.find_element_by_id('login-submit-button').click()
        driver.switch_to.default_content()
        try:
            element = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.ID, 'text-input-what'))
            )
        except:
            raise NameError('Could not log in')
        
        
        
    def jobSearchPage(self):
        # search by ID, class, name
        search = driver.find_element_by_id('text-input-what')
        # type in search
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(Keys.DELETE)
        search.send_keys(JOB_TITLE)
        # search by ID, class, name
        search = driver.find_element_by_id('text-input-where')
        # type in search
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(Keys.DELETE)
        search.send_keys(JOB_LOCATION)
        # hit return
        search.send_keys(Keys.RETURN)

    def jobListingPage(self):
        def filterJobsSearch():
            # find dropdown
            xpath="//ul[@id=\"filter-dateposted-menu\"]/li[@onmousedown=\"rbptk('rb', 'dateposted', '3');\"]/a"        
            search = driver.find_element_by_xpath(xpath)
            date_URL=search.get_attribute('href')
            driver.get(date_URL)
        def getJobBlock():
            ############# Get job block
            time.sleep(3)
            # get a list of all job blocks by class
            xpath="//div[contains(@class,'jobsearch-SerpJobCard unifiedRow row result clickcard')]"  
            jobs_elements = driver.find_elements_by_xpath(xpath)
            #This will be a for loop, invoke apply job
            job_element=jobs_elements[1]
            return jobs_elements
        def clickApply(job_element):
            ############## Hit Apply Now
            #click job frame in block
            xpath="./h2[@class='title']/a"
            job_element.find_element_by_xpath(xpath).click()
            #switch to iframe for apply button
            time.sleep(3)
            iframes = driver.find_elements_by_tag_name("iframe")
            driver.switch_to.frame(iframes[0])
            #click apply button
            xpath="//button[@class='icl-Button icl-Button--branded icl-Button--block']"
            apply_button=driver.find_element_by_xpath(xpath).click()
            time.sleep(3)
            #switch back to default iframe
            driver.switch_to.default_content()
        def fillApplication():
            def switchIframe():
                # Switch to first iframe for application block
                iframes = driver.find_elements_by_tag_name("iframe")
                iframe = driver.find_element_by_xpath("//iframe[@title='Job application form container']")
                driver.switch_to.frame(iframe)
                # Switch to second iframe for application form
                iframes = driver.find_elements_by_tag_name("iframe")
                iframe = driver.find_element_by_xpath("//iframe[@title='Job application form']")
                driver.switch_to.frame(iframe)
                # Fill each page
            def inputForm():
                def fillText()
                    #find text classes
                    xpath="//div[contains(@class,'ia-TextScreenerQuestion is-required')]"  
                    text_class_elements = driver.find_elements_by_xpath(xpath)
                    
                    #input to text classes
                    if len(text_class_elements)>0:
                        for text_class_element in text_class_elements:
                            try:
                                xpath="./div/div/label/span/span[1]"
                                header_text = text_class_element.find_element_by_xpath(xpath).text
                                xpath="./div/div/label/span/span[2]"
                                required_text = text_class_element.find_element_by_xpath(xpath).text
                                xpath="./div/div/input[@type='text']"
                                input_element = text_class_element.find_element_by_xpath(xpath)
                                print(header_text+required_text+':')
                                input_element.send_keys(Keys.CONTROL + "a")
                                input_element.send_keys(Keys.DELETE)
                                user_input=input('')
                                print('thank you for input')
                                input_element.send_keys(user_input)
                            except ElementNotInteractableException:
                                print('got it') 
                            except Exception as e: 
                                print(e)
                                print_exc()
                def fillRadios()
                    #find text classes
                    xpath="//div[contains(@class,'ia-SelectScreenerQuestion ia-SelectScreenerQuestion--radio')]"  
                    radio_class_elements = driver.find_elements_by_xpath(xpath)
                    
                    #input to text classes
                    if len(radio_class_elements)>0:
                        for radio_class_element in radio_class_elements:
                            try:
                                xpath="./div/div/label/span/span[1]"
                                header_text = text_class_element.find_element_by_xpath(xpath).text
                                xpath="./div/div/label/span/span[2]"
                                required_text = text_class_element.find_element_by_xpath(xpath).text
                                xpath="./div/div/input[@type='text']"
                                input_element = text_class_element.find_element_by_xpath(xpath)
                                print(header_text+required_text+':')
                                input_element.send_keys(Keys.CONTROL + "a")
                                input_element.send_keys(Keys.DELETE)
                                user_input=input('')
                                print('thank you for input')
                                input_element.send_keys(user_input)
                            except ElementNotInteractableException:
                                print('got it') 
                            except Exception as e: 
                                print(e)
                                print_exc()
                fillText()
                fillRadios()
            def nextPage():
                anotherPage=True
                try: # Try continue buttons
                    try: # Try normal continue
                        time.sleep(3)
                        continue_button = driver.find_element_by_id('form-action-continue')
                        print('using normal continue')
                        continue_button.click()
                        time.sleep(3)
                        # Check if continue worked 
                        try:
                            xpath="//div[@class='icl-TextInput-errorText ia-GlobalErrors-inputValidationErrorText' and text()='Please fix the errors above to continue applying.']"
                            alert_signal = driver.find_element_by_xpath(xpath)
                            print('found alert')
                            # if alert exists, no more Another Page
                            anotherPage=False
                        except:
                            pass
                        
                        return anotherPage
                    except: # Try intervention continue
                        try:
                            xpath="//button[text()='Continue applying']"
                            intervention_continue_button = driver.find_element_by_xpath(xpath)
                            print('using intervention continue')
                            intervention_continue_button.click()
                            # Check if continue worked 
                            try:
                                xpath="//div[@class='icl-TextInput-errorText ia-GlobalErrors-inputValidationErrorText' and text()='Please fix the errors above to continue applying.']"
                                alert_signal = driver.find_element_by_xpath(xpath)
                                print('found alert')
                                # if alert exists, exit
                                raise Exception("Could not continue to next page")
                            except:
                                print('went to alert exception')
                                pass
                            anotherPage=True
                            return anotherPage
                        except: # Submit button page
                            xpath="//button[text()='Apply']"
                            apply_button = driver.find_element_by_xpath(xpath)
                            print('submit page')
                            apply_button.click()
                            anotherPage=False   
                            return anotherPage
                except: 
                    print('Failed to go to next page')
                    anotherPage=False    
                    return anotherPage  
            
            switchIframe()
            page=1
            anotherPage=True
            while anotherPage:
                inputForm()
                anotherPage=nextPage()
                page+=1
                print(anotherPage)
                print(page)
                
        def closePopup():
            try:
                element = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Close']"))
                )
            except:
                NameError('Could not log in')
            # close popup        
            # The button is hidden by div (ElementClickInterceptedException: element click intercepted)
            # Used return instead of click
            #xpath="//button[@class='popover-x-button-close icl-CloseButton']"
            xpath="//button[@aria-label='Close']"
            close = driver.find_element_by_xpath(xpath).send_keys(Keys.RETURN)
            
        
        filterJobsSearch()    
        closePopup()
        job_element_listing=getJobBlock()
        '''
        for job_element in job_element_listing:
            clickApply(job_element)
        '''
        job_element=job_element_listing[0]         
        clickApply(job_element)
        fillApplication()
        
    
        
        
if __name__=='__main__':
    USER_NAME='Njord Soevik'
    JOB_TITLE="Data Analyst"
    JOB_LOCATION="New York, NY"
    USER_EMAIL='njordsoevik@gmail.com'
    USER_PASS='England11'
    USER_PHONE='3013355230'
    USER_CITY='New York, NY'
    USER_JOBTITLE='Senior Analyst II'
    USER_COMPANY='CoEnterprise'
    mySearch = jobSearch()
    mySearch.signIn()
    time.sleep(3)
    mySearch.jobSearchPage()
    time.sleep(3)
    mySearch.jobListingPage()
    time.sleep(3)
    #mySearch.closePopup()
    #mySearch.scrollJob()




      
    ''' Commenting out autofilled fields
    xpath="//input[contains(@class,'icl-TextInput-control icl-TextInput-control--sm')]"  
    input_elements = driver.find_elements_by_xpath(xpath)
    form_input_ids=[]
    for input_element in input_elements:
        input_id=input_element.get_attribute('id')
        form_input_ids.append(input_id)
        
        for input_id in form_input_ids:
            if input_id=='input-applicant.name':
                name = driver.find_element_by_id(input_id)
                name.send_keys(USER_NAME)
            elif input_id=='input-applicant.email':
                name = driver.find_element_by_id(input_id)
                name.send_keys(USER_EMAIL)
            elif input_id=='input-applicant.phoneNumber':
                name = driver.find_element_by_id(input_id)
                name.send_keys(USER_PHONE)
            elif input_id=='input-applicant.location.city':
                name = driver.find_element_by_id(input_id)
                name.send_keys(USER_CITY)
            elif input_id=='input-applicant.jobTitle':
                name = driver.find_element_by_id(input_id)
                name.send_keys(USER_JOBTITLE)
            elif input_id=='input-applicant.companyName':
                name = driver.find_element_by_id(input_id)
                name.send_keys(USER_COMPANYNAME)
            else:
                print(str(input_id)+' Can not recognize, skipping')
        '''