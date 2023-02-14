
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd

import time

desired_capabilities = {
    "platformName": "Android",
    "deviceName": "Samsung Galaxy S9"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

def swipe_down(driver):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width/2, height*0.25, width/2, height*0.1, 500)

def scrape_data(driver):
    # Create lists to store scraped data
    station_name_list = []
    gasoil10price_list = []

    while True:
        carts = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/stationsdetailView")
        # loop through the carts
        for cart in carts:
            try:
                cart.click()
                androidbottom = driver.find_element(AppiumBy.ID, "android:id/button1")
                androidbottom.click()
                # Find the elements you want to scrape
                station_name = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/companyNameTextView").text
                gasoil10price = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/firstCostTextView").text
                station_name_list.append(station_name)
                gasoil10price_list.append(gasoil10price)
                driver.back()
            except:
                clicking = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationIconView")
                clicking.click()
                androidbottom = driver.find_element(AppiumBy.ID, "android:id/button1")
                androidbottom.click()
                # Find the elements you want to scrape
                station_name = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/companyNameTextView").text
                gasoil10price = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/firstCostTextView").text
                station_name_list.append(station_name)
                gasoil10price_list.append(gasoil10price)
                driver.back()

        if driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationdistanceTxtView").text == "‎ 2 KM":
            break
        swipe_down(driver)

    data = {"station_name": station_name_list, "gasoil10price": gasoil10price_list}
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)

scrape_data(driver)

driver.quit()







#     data['STATION_NAME'] = cart_element.find_element(AppiumBy.ID, "com.mahatati.mag:id/companyNameTextView").text
#     data['STATION_LOCATION'] = cart_element.find_element(AppiumBy.ID, "com.mahatati.mag:id/txtaddress").text
#     data['STATION_CITY'] = cart_element.find_element(AppiumBy.ID, "com.mahatati.mag:id/txtaddress").text
#     data['STATION_LOGO'] = cart_element.find_element(AppiumBy.ID, "").text
#     data['GASOIL_10'] = cart_element.find_element(AppiumBy.ID, "com.mahatati.mag:id/firstCostTextView").text
#     data['SUPERCARB_URANT_SANS'] = cart_element.find_element(AppiumBy.ID, "com.mahatati.mag:id/secondCostTextView").text
#     data['GASOIL_PREMIUM'] = cart_element.find_element(AppiumBy.ID, "com.mahatati.mag:id/thirdCostTextView").text
#     data['SSP_PREMIUM'] = cart_element.find_element(AppiumBy.ID, "com.mahatati.mag:id/thirdCostTextView").text
#     data['LAST_UPDATE'] = cart_element.find_element(AppiumBy.ID, "com.mahatati.mag:id/latestDateTextView").text
