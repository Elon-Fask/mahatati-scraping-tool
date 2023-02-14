

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

def scraper_data(driver):
    station_city_list = []
    station_name_list = []
    station_location_list = []
    gasoil10_price_list = []
    supercarb_price_list = []
    last_updated_day_list = []

    while True:
        carts = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/contentLayout")

        for cart in carts:
            # carts = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/stationsdetailView")
            cart.click()
            androidbottom = driver.find_element(AppiumBy.ID, "android:id/button1")
            androidbottom.click()
            # Find the elements you want to scrape
            station_city = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/cityTextView").text
            station_city_list.append(station_city)

            station_name = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/companyNameTextView").text
            station_name_list.append(station_name)

            station_location = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/txtaddress").text
            station_location_list.append(station_location)

            gasoil10_price = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/firstCostTextView").text
            gasoil10_price_list.append(gasoil10_price)

            supercarb_price = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/secondCostTextView").text
            supercarb_price_list.append(supercarb_price)

            last_updated = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/latestDateTextView").text
            last_updated_day_list.append(last_updated)

            driver.back()
            time.sleep(2)
            swipe_down(driver)

        if driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationdistanceTxtView").text == "‎ 3 KM":
            break
        # swipe_down(driver)
        time.sleep(2)
    data = {
        "CITY": station_city_list,
        "STATION NAME": station_name_list,
        "STATION_LOCATION": station_location_list,
        "GASOIL10 PRICE": gasoil10_price_list,
        "SUPERCARB_URANT_SANS": supercarb_price_list,
        "LAST UPDATED": last_updated_day_list

    }
    df = pd.DataFrame(data)
    df.to_csv('scraped.csv', index=False)
    print(df)

scraper_data(driver)
driver.quit()