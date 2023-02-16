import pandas as pd
import time

#df1 = pd.read_csv("/home/elon-fask/Desktop/mahatati-scraper/all_csv/mahatati_data_supercarb.csv")
#df2 = pd.read_csv("/home/elon-fask/Desktop/mahatati-scraper/all_csv/mahatati_data.csv")

#df2 = pd.merge(df1, df2, left_on='station_name', right_on='station_name')


#df2.to_csv("mahatati_all_data_casa_50km_rang.csv", index=False)

print("merging the gasoil10 and supercarburant prices into one ultimate csv file. ")
time.sleep(2)

gasoil10 = input("path to gasoil10 .csv (example: /home/username/file1.csv) =>  ")
supercarburant = input("path to supercarburant .csv =>  ")

df1 = pd.read_csv(gasoil10)
df2 = pd.read_csv(supercarburant)

df3 = pd.merge(df1, df2, left_on='station_name',right_on='station_name')


name_your_final_file = input("name your file: ")

df3.to_csv(name_your_final_file + ".csv", index=False)
