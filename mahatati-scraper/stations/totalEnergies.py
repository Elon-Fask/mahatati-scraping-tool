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
        if driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationdistanceTxtView").text == "‎ 38 KM":
            break
        # if driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[8]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView[3]").text == "‎ 48 KM":
        #     break

    df = pd.DataFrame({
        "city": "Casablanca",
        "company": "TOTAL ENERGIES",
        "station_name": station_name_list,
        "gasoil10_price": gasoil10_price_list,
        "station_location": station_location_list
    })
    df.to_csv("mahatati_data_gasoil10_total_energies.csv", index=False)

    print("Done")
    print(df)

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
        if driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationdistanceTxtView").text == "‎ 38 KM":
            break
        # if driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[8]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView[3]").text == "‎ 48 KM":
        #     break

    df = pd.DataFrame({
        "city": "Casablanca",
        "company": "TOTAL ENERGIES",
        "station_name": station_name_list,
        "supercarburant_price": supercarburant_price_list,
        "station_location": station_location_list
    })
    df.to_csv("mahatati_data_supercarburant_total_energies.csv", index=False)

    print("Done")
    print(df)

print("Starting ...")
time.sleep(2)
choose = input("Choose 1 for gasoil10 price or 2 for supercarburant price: ")
if choose == "1":
    if driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/essenceOilTxtView").text == "GASOIL 10":
        scraper_data_gasoil10_price(driver)
    else:
        raise Exception("Gasoil 10 not found")
elif choose == "2":
    if driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/essenceOilTxtView").text == "SUPERCARBURANT SANS PLOMB":
        scraper_data_supercarburant_price(driver)
    else:
        raise Exception("Supercarburant not found")


# df1 = pd.read_csv("mahatati_data_gasoil10_total_energies.csv")
# df2 = pd.read_csv("mahatati_data_supercarburant_total_energies.csv")
#
# df3 = pd.merge(df1, df2, on=['city', 'company', 'station_name', 'station_location'], how='outer')
# df3.to_csv("mahatati_data_casa_total_energies.csv", index=False)


driver.quit()