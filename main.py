# Selenium WebDriver Python coding
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
# The Select library operates the drop down list.
from selenium.webdriver.support.ui import Select
import time

exec_path = r"chromedriver.exe"
URL = "https://inderpsingh.blogspot.com/2014/08/demowebapp_24.html"
distance_id_locator = "distance"
distance = 0 # Assign some initial value to distance.
speed_id_locator = "speed"
speed = 45 # Assign some initial value to speed.
time_id_locator = "hours"
calculate_css_locator = ".post-body > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > button:nth-child(20)"
result_id_locator = "result"
wait_time_out = 5

# Define the Python WebDriver
driver = webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
wait_variable = W(driver, wait_time_out)
# JavaScript to scroll window down by 240 pixels
driver.execute_script("window.scrollBy(0,240)", "")
# Find web elements using WebDriverWait Python.
distance_element = wait_variable.until(E.presence_of_element_located((By.ID, distance_id_locator)))
speed_element = wait_variable.until(E.presence_of_element_located((By.ID, speed_id_locator)))
# Time_element is a drop down list. Call the Select method on Explicit Wait.
time_element = Select(wait_variable.until(E.presence_of_element_located((By.ID, time_id_locator))))
calculate_element = wait_variable.until(E.presence_of_element_located((By.CSS_SELECTOR, calculate_css_locator)))
result_element = wait_variable.until(E.presence_of_element_located((By.ID, result_id_locator)))
# time_element.options is the list of all the options in the dropdown list.
for option in time_element.options:
    distance_element.clear()
    distance += 100 # Generate distance test data by adding 100 to it's previous value.
    distance_element.send_keys(distance)
    speed_element.clear()
    speed += 1 # Generate speed test data by adding 1 to it's previous value.
    speed_element.send_keys(speed)
    time_element.select_by_visible_text(option.text) # Select the dropdown option.
    calculate_element.click()
    time.sleep(1)
    # Calculate the expected result using my own calculation.
    expected_result = round(float(distance)/float(speed)/float(option.get_attribute("value")),4)
    if expected_result == int(expected_result): expected_result = int(expected_result)
    # Validate by comparing expected result with the actual result from the application.
    if str(expected_result) in result_element.text:
        print ("Passed", str(expected_result), result_element.text)
    else:
        print ("Failed", str(expected_result), result_element.text)