from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

""" 
Initiate the browser by opening a new chrome window.
This is the aws bot test for crawling through S3 data.
"""
browser  = webdriver.Chrome(ChromeDriverManager().install())

# Visit the page you want to go to.

browser.get('https://aws.amazon.com/console/')

# click on Log in
browser.find_element_by_class_name('lb-btn-p-primary').click();

# Your aws credentials
aws_name = os.environ.get("AWS_NAME")
aws_pass = os.environ.get("AWS_PASS")

# Fill credentials
browser.find_element_by_class_name('aws-signin-textfield')
browser.find_element_by_name(“pass”).send_keys(fb_pass)
# Click Log In
browser.find_element_by_id('loginbutton').click();