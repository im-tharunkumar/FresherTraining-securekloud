#Read and merge 2 CSV files and write them in a single file. 
#For example, the first CSV can have employee details, 
#and the second one can have their number of experiences (one-to-one relationship).

import pandas as pd
import logging

logging.basicConfig(filename='mergecsv.log',filemode='w',level=logging.DEBUG,
                    format= '%(asctime)s :: %(levelname)s :: %(message)s')

csv1=input("Enter the first csv path:\n")       #Read csv 1
csv2=input("Enter the second csv path:\n")      #Read csv2
newFile=input("Enter the new file path:\n")     #read new file path

data1=pd.DataFrame(pd.read_csv(csv1))       #read all data in csv1 as dataframe 
data2=pd.DataFrame(pd.read_csv(csv2))       #read all data in csv2 as datarame

if data1.shape[0]==data2.shape[0]:
    mergedData=pd.merge(data1,data2,validate='1:1') #merge two dataframe
    mergedData.to_csv(newFile,index=False) #write merged dataframe into new file
    logging.debug('Both files have same number of rows')
else:
    logging.error('Two file does not have same number of rows')


print("Data from the merged file:\n")

cn=pd.read_csv(newFile)      #print new  csv file
print(cn)

