#Program to read a CSV file, convert it to JSON, and save it in another file
import csv
import json

csv_file=input("Enter CSV path:\n")                 #geting csv file path - username.csv for example
new_file=input("Enter new file path:\n")            #getting new file path

with open(csv_file) as cf:
    data_from_csv=list(csv.DictReader(cf))          #reading data from csv as list
    with open(new_file,'w') as nf:
        for i in data_from_csv:
            data_in_json=json.dumps(i,indent = 0)    #converting list into json 
            nf.write(data_in_json)                     # writing json into new file

                
print("Data from new file:\n")

with open(new_file) as nf:          #diplay data from new file
    print(nf.read())