import selenium
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

import time

from selenium.webdriver.support.wait import WebDriverWait

desired_capabilities = {
    "platformName": "Android",
    "deviceName": "Samsung Galaxy S9"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

def swipe_down(driver):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width/2, height*0.22, width/2, height*0.1, 500)

def scraper_data(driver):
    station_name_list = []
    station_location_list = []
    gasoil10_price_list = []

    while True:
        station_name = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationNameTxtView").text
        gasoil10_price = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/gasoilunitTxtView").text
        station_location = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationAvenvueTxtView").text
        station_name_list.append(station_name)
        gasoil10_price_list.append(gasoil10_price)
        station_location_list.append(station_location)
        swipe_down(driver)
        if driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationdistanceTxtView").text == "‎ 48 KM":
            break
    df = pd.DataFrame({
        "city": "Casablanca",
        "station_name": station_name_list,
        "gasoil10_price": gasoil10_price_list,
        "station_location": station_location_list
    })
    df.to_csv("mahatati_data.csv", index=False)

    print("Done")
    print(df)


scraper_data(driver)
driver.quit()