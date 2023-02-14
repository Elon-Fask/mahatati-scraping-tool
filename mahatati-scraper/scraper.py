import csv
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd

desired_capabilities = {
    "platformName": "Android",
    "deviceName": "Samsung Galaxy S9"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)


# Define a function to swipe down the screen
def swipe_down(driver):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width/2, height*0.25, width/2, height*0.1, 500)

def scrape_data(driver):

    # Find the elements you want to scrape
    station_name = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/companyNameTextView")
    gasoil10price = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/firstCostTextView")

    # Create a list to store the scraped data
    station_name_list = []
    gasoil10price_list = []

    for element in station_name:
        station_name_list.append(element.text)
    for element in gasoil10price:
        gasoil10price_list.append(element.text)

    # Create a DataFram to store the scraped data
    df = pd.DataFrame({
        'station_name': station_name_list,
        'gasoil10price': gasoil10price_list
    })

    # Save the scraped data to a csv file
    df.to_csv('data.csv', index=False)

# start scraping data
while True:
    # find carts
    carts = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/stationsdetailView")
    # loop through the carts
    for cart in carts:
        # click on the cart
        cart.click()
        # click on the android bottom
        androidbottom = driver.find_element(AppiumBy.ID, "android:id/button1")
        androidbottom.click()
        # scrape the data
        scrape_data(driver)
        # go back to the previous page
        driver.back()

    limit = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/stationdistanceTxtView")
    if limit[0].text == "‎ 2 KM":
        break

    swipe_down(driver)

driver.quit()








