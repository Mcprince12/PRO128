#Importing libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

#Get page requests
page_ = requests.get(url)
print(page_)

soup = BeautifulSoup(page_.text,'html.parser')

starTable = soup.find_all('table')
print(len(starTable))

#Defining templist array and finding specifics
tempList= []
table_rows = starTable[4].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)
print(tempList)

names = []
distance=[]
mass=[]
radius=[]
#For loop, appending the temp_list
for i in range(1,len(tempList)):
    names.append(tempList[i][0])
    distance.append(tempList[i][5])
    mass.append(tempList[i][7])
    radius.append(tempList[i][8])
df = pd.DataFrame(list(zip(names, distance, mass, radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df)

#Converting to csv
df.to_csv('dwarfStars.csv')