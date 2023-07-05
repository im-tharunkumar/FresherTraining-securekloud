"""import csv
with open("sample.csv") as cf:
    data=csv.reader(cf)
    for i in data:
        print(i)"""
        
"""import pandas as pd

cf=pd.read_csv("sample.csv")
print(cf)"""

import json

with open("1.json") as jf:
    data=json.load(jf)
print(data)

'''
import csv

print("data from reader fun: \n")
with open("sample.csv") as cc:
    data=csv.reader(cc)
    for i in data:
        print(i)

print("data from Dictreader fun: \n")
with open("sample.csv") as cf:
    data1=csv.DictReader(cf)
    for i in data1:
        print(i)
    '''
'''
import json

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('person.json', 'w') as json_file:
  json.dump(person_dict, json_file)
    '''
    
    