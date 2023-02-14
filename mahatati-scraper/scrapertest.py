from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
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
    driver.swipe(width/2, height*0.8, width/2, height*0.2, 1000)

# Define a function to scrape the data from each cart
def scrape_data(driver):
    # Define the elements you want to scrape and store them in a list
    elements = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationsdetailView").click()

    botton1 = driver.find_element(AppiumBy.ID, "android:id/button1")
    botton1.click()
    
    data = []
    for element in elements:
        data.append(element.text)
    return data

# Define a function to click on each cart
def click_cart(driver):
    carts = driver.find_elements(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.example.android.your_cart_id']")
    for cart in carts:
        cart.click()

# Define a function to export the data to a CSV file
def export_to_csv(data):
    df = pd.DataFrame(data, columns=["First_Data", "Second_Data", "Third_Data", "Fourth_Data", "Fifth_Data"])
    df.to_csv("scraped_data.csv", index=False)

# Start the scraping process
all_data = []
while True:
    # Scrape the data from each cart
    data = scrape_data(driver)
    all_data.extend(data)

    # Check if the end of the data has been reached
    if driver.page_source.find("No more data to display") != -1:
        break

    # Scroll down to the next page of data
    swipe_down(driver)

# Export the data to a CSV file
export_to_csv(all_data)

# Close the driver
driver.quit()





# content = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/stationsdetailView")
# content.click()
#
# botton1 = driver.find_element(AppiumBy.ID, "android:id/button1")
# botton1.click()
#
# # prices = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/gasoilunitTxtView")
#
# price = driver.find_element(AppiumBy.ID, "com.mahatati.mag:id/firstCostTextView")
# print(price.text)











# def swipe_down(driver):
#     previous_height = driver.execute_script("return document.body.scrollHeight")
#     width = driver.get_window_size()['width']
#     height = driver.get_window_size()['height']
#     driver.swipe(width/2, height*0.8, width/2, height*0.2, 1000)
#     current_height = driver.execute_script("return document.body.scrollHeight")
#     if previous_height == current_height:
#         return False
#     return True

# data = []
# while True:
#     prices = driver.find_elements(AppiumBy.ID, "com.mahatati.mag:id/gasoilunitTxtView")
#     for price in prices:
#         data = price.text
#         data.append(price)
#     # Scroll down
#     # swipe_down(driver)
#     #
#     # if not swipe_down(driver):
#     #     break
#
#
#
#
# # Use pandas to export the data to an excel file
#
# df = pd.DataFrame(data)
# df.to_excel("data.xlsx", index=False)
#
# driver.quit()