
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd

import time


# Create an instance of the Appium driver
driver = webdriver.Remote(
    "http://localhost:4723/wd/hub",
    desired_capabilities={
    "platformName": "Android",
    "deviceName": "Samsung Galaxy S9"
    }
)

# Define a function to swipe down the screen
def swipe_down(driver):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width/2, height*0.3, width/2, height*0.1, 500)


def scrape_data(driver):

    # Find the elements you want to scrape
    station_name = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/companyNameTextView")
    gasoil10price = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/firstCostTextView")

    # Create a list to store the scraped data
    station_name_list = []
    gasoil10price_list = []

    carts = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/stationsdetailView")
    # Loop through the elements to be clicked on
    for cart in carts:
        # Click on the element
        cart.click()
        androidbottom = driver.find_element(AppiumBy.ID, "android:id/button1")
        androidbottom.click()

        # scrape the data from element
        for element in station_name:
            station_name_list.append(element.text)
        for element in gasoil10price:
            gasoil10price_list.append(element.text)
    time.sleep(2)
    driver.back()

    # Create a DataFram to store the scraped data
    df = pd.DataFrame({
        'station_name': station_name_list,
        'gasoil10price': gasoil10price_list
    })

    # Save the scraped data to a csv file
    df.to_csv('data.csv', index=False)

def swipe_down(driver):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    driver.swipe(width/2, height*0.25, width/2, height*0.1, 500)



# start the scraping process
while True:
    # find the carts and click on each one
    carts = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/stationsdetailView")
    for cart in carts:
        limit = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationdistanceTxtView")
        if limit.text == "‎ 2 KM":
            break
        carts = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/stationsdetailView")
        cart.click()
        androidbottom = driver.find_element(AppiumBy.ID, "android:id/button1")
        androidbottom.click()
        scrape_data(driver)

        swipe_down(driver)

    # swipe_down(driver)

    # swipe_down(driver)

    driver.quit()







#     carts = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/stationsdetailView")
#
#     # elements1 = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/companyNameTextView")
#     # elements2 = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/firstCostTextView")
#
#     for cart in carts:
#         cart.click()
#         botton1 = driver.find_element(AppiumBy.ID, "android:id/button1")
#         botton1.click()
#
#         elements1 = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/companyNameTextView")
#         elements2 = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/firstCostTextView")
#         for element1, element2 in zip(elements1, elements2):
#             data1.append(element1.text)
#             data2.append(element2.text)
#
#         driver.back()
#         # Swipe down to show the next set of data
#         swipe_down(driver)
#
#         # Wait for the page to load
#         time.sleep(2)
#
#         # Repeat the process until you have scraped all the data
#         return data1, data2
#
#
#
#
# # Create a pandas DataFrame to store the scraped data
# data_dict = {'Column 1': all_data1, 'Column 2': all_data2}
# df = pd.DataFrame(data_dict)
#
# # Export the data to a CSV file
# df.to_csv('scraped_data.csv', index=False)
#
# # Close the Appium session
# driver.quit()
#
