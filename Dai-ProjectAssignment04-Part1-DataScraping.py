#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:37:44 2023

@author: lingyundai
"""

# import libraries
import requests
import json
import pandas as pd

# parse page by in network tab api/rankings because the website is written in 
# javascript and the ranking does not fully load until further scrolls
# so to parse the response payload, I need a couple of urls to parse 
# all data on the web page

# row 0 to 99
url_1 = "https://www.openpowerlifting.org/api/rankings/uspc/women/2023/by-total?start=0&end=99&lang=en&units=kg"
# row 100 to 199
url_2 = "https://www.openpowerlifting.org/api/rankings/uspc/women/2023/by-total?start=100&end=199&lang=en&units=kg"
# row 200 to 299
url_3 = "https://www.openpowerlifting.org/api/rankings/uspc/women/2023/by-total?start=200&end=299&lang=en&units=kg"
# row 300 to 335 (last row)
url_4 = "https://www.openpowerlifting.org/api/rankings/uspc/women/2023/by-total?start=300&end=335&lang=en&units=kg"

# load the json responses
# row 0 to 99
response_1 = requests.get(url_1)
data_1 = json.loads(response_1.text)
# row 100 to 199
response_2 = requests.get(url_2)
data_2 = json.loads(response_2.text)
# row 200 to 299
response_3 = requests.get(url_3)
data_3 = json.loads(response_3.text)
# row 300 to 335 (last row)
response_4 = requests.get(url_4)
data_4 = json.loads(response_4.text)

# get the data for each rows/lifters from the json payload
# row 0 to 99
rows_1 = data_1.get("rows")
# row 100 to 199
rows_2 = data_2.get("rows")
# row 200 to 299
rows_3 = data_3.get("rows")
# row 300 to 335 (last row)
rows_4 = data_4.get("rows")

# headers match the sequence of headers on the web page
headers = ["Rank", "Lifter", "Fed", "Date", "Location", "Sex",
           "Age", "Equip", "Class", "Weight", "Squat", "Bench", 
           "Deadlift", "Total", "Dots"]

# the indices are the same sequence in headers
selectedIndices = [1, # Rank
                   2, # Lifter
                   8, # Fed
                   9, # Date
                   7, # Location
                   13, # Sex
                   15, # Age
                   14, # Equip
                   18, # Class
                   17, # Weight
                   19, # Squat
                   20, # Bench
                   21, # Deadlift
                   22, # Total
                   23 # Dots
                   ]

# parse the indices to corresponding header
class ParserHelper:
    def __init__(self):
        pass
    
    def parseRowsAndSelectData(self, rows, selectedIndices):
        selectedData = []
        for row in rows:
            curRow = []
            for i in selectedIndices:
                if i == 7 and row[i] == None:
                    curRow.append(f"{row[10]}-{row[11]}")
                else:
                    curRow.append(row[i])
            
            selectedData.append(curRow)
        
        return selectedData

# call helper function
obj = ParserHelper()
# collect parsed data to parsedData array
parsedData = []
res_1 = obj.parseRowsAndSelectData(rows_1, selectedIndices)
parsedData.extend(res_1)
res_2 = obj.parseRowsAndSelectData(rows_2, selectedIndices)
parsedData.extend(res_2)
res_3 = obj.parseRowsAndSelectData(rows_3, selectedIndices)
parsedData.extend(res_3)
res_4 = obj.parseRowsAndSelectData(rows_4, selectedIndices)
parsedData.extend(res_4)

# write to csv file
dataset = pd.DataFrame(data=parsedData, columns=headers)
dataset.to_csv("Dai-ProjectAssignment04.csv", index=False)
