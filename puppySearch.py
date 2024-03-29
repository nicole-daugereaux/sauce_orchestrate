####################################################################
# Skeleton for Selenium tests on Sauce Labs
####################################################################

###################################################################
# Imports that are good to use
###################################################################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import multiprocessing
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
# This makes the functions below execute 'run' amount of times
###################################################################
run = 25
###################################################################
# Declare as a function in order to do multiple runs
###################################################################
def run_sauce_test():

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
    options.platform_name  = 'Windows 10'
    options.add_argument("--deny-permission-prompts")

    sauceParameters = {
        # Sauce Specific Options
            'tags':[''],
            'build': 'Sauce Orchestrate w/ Docker',
            'name': 'Sauce Orchestrate w/ Docker',
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

    driver.get('https://www.duckduckgo.com')
    interact = driver.find_element("id","searchbox_input")
    interact.clear()
     # # # Using the selected element
    interact.send_keys('puppies')
    interact.submit()


    count = 0
    while count < 3000:
      # Your code here
      interact1 = driver.find_element("id","search_form_input")
      # interact1.clear()
      # # # # Using the selected element
      # interact1.send_keys('puppies')
      # interact1.submit()
      count += 1


    # Setting the job status to passed
    driver.execute_script('sauce:job-result=passed')

    # Ending the test session
    driver.quit()

###################################################################
# Run the above code in parallel
###################################################################

if __name__ == '__main__':
    jobs = [] # Array for the jobs
    for i in range(run): # Run the amount of times set above
        jobRun = multiprocessing.Process(target=run_sauce_test) # Define what function to run multiple times.
        jobs.append(jobRun) # Add to the array.
        jobRun.start() # Start the functions.
        # print('this is the run for: '+ str(i))
