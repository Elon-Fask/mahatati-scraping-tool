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

def scraper_data_gasoil10_price(driver):
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
        if driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationdistanceTxtView").text == "‎ 42 KM":
            break
        # if driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[8]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView[3]").text == "‎ 43 KM":
        #     break

    df = pd.DataFrame({
        "city": "Casablanca",
        "company": "AFRIQUIA",
        "station_name": station_name_list,
        "gasoil10_price": gasoil10_price_list,
        "station_location": station_location_list
    })
    df.to_csv("mahatati_data_gasoil10_AFRIQUIA.csv", index=False)

    print(df)
    print("Done")

def scraper_data_supercarburant_price(driver):
    station_name_list = []
    station_location_list = []
    supercarburant_price_list = []

    while True:
        station_name = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationNameTxtView").text
        supercarburant_price = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/essenceunitTxtView").text
        station_location = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationAvenvueTxtView").text
        station_name_list.append(station_name)
        supercarburant_price_list.append(supercarburant_price)
        station_location_list.append(station_location)
        swipe_down(driver)
        if driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationdistanceTxtView").text == "‎ 42 KM":
            break
        # if driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[8]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView[3]").text == "‎ 48 KM":
        #     break

    df = pd.DataFrame({
        "city": "Casablanca",
        "company": "AFRIQUIA",
        "station_name": station_name_list,
        "supercarburant_price": supercarburant_price_list,
        "station_location": station_location_list
    })
    df.to_csv("mahatati_data_supercarburant_AFRIQUIA.csv", index=False)

    print(df)
    print("Done")

def merge_csv():
    df1 = pd.read_csv("mahatati_data_gasoil10_AFRIQUIA.csv")
    df2 = pd.read_csv("mahatati_data_supercarburant_AFRIQUIA.csv")

    df2 = pd.merge(df1, df2, left_on="station_name", right_on="station_location")
    df2.to_csv("AFRIQUIA_all_data_mahatati.csv", index=False)
    print(df2)

print("Starting ...")
time.sleep(2)
choose = input("Choose 1 for GASOIL10 or 2 for SUPERCARBURANT SANS POMB / choose 3 to merge them : ")
if choose == "1":
    if driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/gasOilTxtView").text == "GASOIL 10":
        print("wait ...")
        scraper_data_gasoil10_price(driver)
    else:
        raise Exception("Gasoil 10 not found")
elif choose == "2":
    if driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/essenceOilTxtView").text == "SUPERCARBURANT SANS PLOMB":
        print("wait ...")
        scraper_data_supercarburant_price(driver)
    else:
        raise Exception("Supercarburant not found")
elif choose == "3":
    merge_csv()
    print("Done")

driver.quit()