# Call any one of the open APIs from https://any-api.com and write the output in a CSV file

import csv,requests

#requesting open api that return json of bank holidays in uk for 2018-2025 years 

response=requests.get('https://www.gov.uk/bank-holidays.json') #here respomse will be code like 200,404

Data=response.json() #reading json data

keys=[] #list to store in csv

#converting that nested json into simple list as we want

for i,j in Data.items(): #country name i=england and wales,scotland,northern-ireland
    for x,z in j.items(): #j=division,event[]
        if isinstance(z, list):#x=events thats is where data we need is stored
            for d in z: #every element d in list z will be dict
                temp=[]
                for g,h in d.items(): #g will be key that is title,date,notes,bunting h is values
                    if isinstance(h,str) and h !='': #emlimating boolean and empty string values
                        temp.append(h)  #reading data we need and appending in temp list
                cs=i +','+','.join(temp) #combining data as format that need
                keys.append(cs) #appending to final list
                    
with open('DataforAPI.csv','w',newline='') as cf: #if we not use newline all data will be stored in single line
    reader=csv.writer(cf) 
    for i in keys:
        reader.writerow(i.split(',')) #if we not use split here then value will be stored within ""

print("Data written within 'Dataforapi.csv' file:\n")