#importing packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

#instantiating chrome driver object
#path needs to be changed as per the local system
driver = webdriver.Chrome(executable_path = 'C:\\Users\\Kashif\\Documents\\Selenium Jar\\chromedriver.exe')

## Function to validate login functionality of HUDL
def validate_hudl_login(email_id, password, driver, message, remember_me=False):
    
    #launching hudl.com
    driver.get("https://www.hudl.com")
    
    time.sleep(2)     #2 seconds time delay
    
    #redirecting to hudl.com login page
    login_page_button = driver.find_elements_by_class_name("login")[0]
    login_page_button.click()

    time.sleep(2)    #2 seconds time delay

    #login email input
    email_id_input_box = driver.find_element_by_id("email")

    #login password input
    password_input_box = driver.find_element_by_name("password")

    
    #clear the placeholders
    email_id_input_box.clear()
    password_input_box.clear()
    
    #fill login credentials
    email_id_input_box.send_keys(email_id)
    
    time.sleep(2)    #2 seconds time delay
    
    password_input_box.send_keys(password)
    
    time.sleep(2)  #2 seconds time delay
    
    #to click remember me functionality
    if remember_me:
        element = driver.find_element_by_xpath('//*[@id="remember-me"]')
        driver.execute_script("arguments[0].click();", element)
      
    time.sleep(2)    #2 seconds time delay
    
    #login through site
    login_button = driver.find_element_by_id("logIn")
    login_button.click()
    
    #wait the ready state to be complete
    WebDriverWait(driver = driver, timeout = 20).until(lambda x: x.execute_script("return document.readyState === 'complete'"))
    error_message = "We didn't recognize that email and/or password. Need help?"
   
    
    time.sleep(2)#2 seconds time delay
    
    #if error message found, then login is failed
    if driver.find_elements_by_class_name("fade-in-expand") and error_message == driver.find_elements_by_class_name("fade-in-expand")[0].text:
        print("Login Failed with {0}".format(message))
    else:
        print("Login Successful with {0}".format(message))
    #-----------------------------------------------------------------------------------
    #driver.close() #to close chrome driver

## Function to Logout from Hudl
def logout_hudl(driver):
    
    time.sleep(5)

    element = driver.find_element_by_xpath('//*[@id="ssr-webnav"]/div/div[1]/nav[1]/div[4]/div[2]/div[2]/div[3]/a')
    driver.execute_script("arguments[0].click();", element)
    
    print("Successfully Logout")


## TestCase-1 Login with valid credential
## Note: Kindly provide valid credential
#hudl valid credentials
email_id = "<YOUR VALID EMAIL ID>"
password = "<YOUR VALID PASSWORD>"

#calling validatehudllogin method/function to validate login with given credential
validate_hudl_login(email_id, password, driver, "Valid Credential")
logout_hudl(driver)

## TestCase-2 Login with invalid credential
#hudl credentials
email_id = "<YOUR INVALID EMAIL ID>"
password = "<YOUR INVALID PASSWORD>"

#calling validatehudllogin method/function to validate login with given credential
validate_hudl_login(email_id, password, driver, "Invalid Credential")

## TestCase-3 Login with empty credential
#hudl credentials
email_id = ""
password = ""

#calling validatehudllogin method/function to validate login with given credential
validate_hudl_login(email_id, password, driver, "Empty Credential")

## TestCase-4 Login with valid credential with remember me functionality
#hudl credentials
email_id = "<YOUR VALID EMAIL ID>"
password = "<YOUR VALID PASSWORD>"

#calling validatehudllogin method/function to validate login with given credential
validate_hudl_login(email_id, password, driver, "Valid Credential and Remember me",True)
logout_hudl(driver)

#redirecting to hudl.com login page
login_page_button = driver.find_elements_by_class_name("login")[0]
login_page_button.click()
time.sleep(2)
remember_me_email = driver.find_element_by_id("email").get_attribute("value")
if email_id ==  remember_me_email:
    print("Remember me Functionality Validation Successful!")
else:
    print("Remember me Functionality Validation Unsuccessful!")

