####################################################################
# Skeleton for Selenium tests on Sauce Labs
####################################################################

###################################################################
# Imports that are good to use
###################################################################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep
import os
import urllib3
import json
import random

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
###################################################################
# Select Data Center
# Set region to 'US' or 'EU'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################
region = 'US'
###################################################################
# Test Configuration Options
options = ChromeOptions()
options.browser_version = '114'
options.platform_name  = 'MacOS 12'
sauceParameters = {
    # Sauce Specific Options
        'tags':[''],
        'build': 'Sauce Orchestrate',
        'name': 'Sauce Orchestrate Demo',
        'seleniumVersion': '4',
}
options.set_capability('sauce:options', sauceParameters)

###################################################################
# Connect to Sauce Labs
try:
    region
except NameError:
    region = 'EU'

if region == 'US':
    print('You are using the US data center for a Desktop test, rockstar!')
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        options=options)
elif region == 'EU':
    print ('You are using the EU data center for a Desktop test, you beautiful tropical fish!')
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        options=options)

###################################################################
# Test logic goes here
###################################################################
# Navigating to a website and doing the same thing over and over to replicate a long test

driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
#
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()


driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
driver.get('https://www.google.com')
interact = driver.find_element("id","APjFqb")
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()
#


# Setting the job status to passed
driver.execute_script('sauce:job-result=passed')

# Ending the test session
driver.quit()
