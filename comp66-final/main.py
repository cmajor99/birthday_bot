#Ryan Steele - 4291461
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import inspect
from query import birthdayCheck,grabPhone,unpackTuple, grabEmail
from sms import sendSMS
from email_send import emailSequence

def mainFunc():
    #path to webdrive in use
    browser = webdriver.Chrome(executable_path ="/usr/bin/chromedriver") 

    website_URL ="https://www.facebook.com/"
    browser.get(website_URL)
    # user name or e-mail  
    username = "steele.ryansteven@gmail.com"
    
    #getting password from text file - create your own to test 
    with open('test.txt', 'r') as myfile: 
        password = myfile.read().replace('\n', '') 

    #Confirmation    
    print("Let's Begin") 

    #find the username/email entry field  
    element = browser.find_elements_by_xpath('//*[@id ="email"]') 
    element[0].send_keys(username) 

    #Confirmation  
    print("Username Entered") 
    
    element = browser.find_element_by_xpath('//*[@id ="pass"]') 
    element.send_keys(password) 

    #Confirmation  
    print("Password Entered") 
    
    #logging in 
    log_in = browser.find_elements_by_id('loginbutton') 
    log_in[0].click() 
    
    print("Login Successfull")  
    website_URL ="https://www.facebook.com/events/birthdays/"
    browser.get(website_URL)
    #implicit wait in case the connection is slow
    browser.implicitly_wait(2)
    #load the birthday check function into a variable to test
    names_list = birthdayCheck()
    print(names_list)
    #Iterate through the list of names returned from the DB
    for f_name,l_name in names_list:
        #test each tuple named pair for a birthday on the page
        birthdays = (browser.find_elements_by_link_text("%s %s"% (f_name,l_name)))
        if len(birthdays) > 0:

            phone = grabPhone(f_name,l_name)
            email_ = grabEmail(f_name,l_name)

            if len(phone) > 0:
                sendSMS(f_name,phone)
                print(f'Phone number found: {phone}')
                print('SMS Sent')
            else:
                print('No Phone number')
            if len(email_) > 0:
                emailSequence(f_name,l_name,email_)
                print(f'Email found: {email_}')
                print('Email Sent')
            else:
                print('No email')

        else:
            print('Not their birthday')
    browser.close()

test = mainFunc()