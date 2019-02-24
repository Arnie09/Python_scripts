import pandas as pd
from bs4 import BeautifulSoup
import os
import sys
outputpath = os.path.join(sys.path[0])
path = os.path.join(sys.path[0],'html/sample.html')
data = []

''' getting the header '''
header_data = []
soup = BeautifulSoup(open(path),'html.parser')
header = soup.find_all("table")[0].find("tr")
for items in header:
    header_data.append(items.get_text())

''' getting the data '''
dataHtml = soup.find_all("table")[0].find_all("tr")[1:]
for items in dataHtml:
    sub_data = []
    for sub_items in items:
        sub_data.append(sub_items.get_text())
    data.append(sub_data)

''' generating and storing dataFrame'''
dataFrame = pd.DataFrame(data=data,columns = header_data)
dataFrame.to_csv(os.path.join(outputpath,'data.csv'))
