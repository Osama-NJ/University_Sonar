import time
from selenium import webdriver

# Setting up Web Driver
driver = webdriver.Chrome("chromedriver.exe")


def find_university():
    """
    This function finds the Nearest University.
    """
    driver.get("https://www.google.com/maps")  # Open Google maps
    time.sleep(2)
    land = driver.find_element_by_class_name("tactile-searchbox-input")  # Finding the search-bar
    land.send_keys("University near me")  # Sending the phrase into the search-bar
    find_button = driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]')  # Finding the search submit button
    find_button.click()  # Clicking on the search submit button


find_university()  # Calling the find_land function


def nearest_route():
    """
    This function gets nearest route for the university.
    """
    time.sleep(7)
    route = driver.find_element_by_xpath('//*[contains(@src,"ic_directions_gm_blue_24px.png")]')  # Finding direction button
    route.click()  # Clicking on direction button


nearest_route()  # Calling nearest_route function
