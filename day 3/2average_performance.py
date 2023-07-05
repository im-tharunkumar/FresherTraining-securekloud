#Program to read 2 CSV files, merge them, and aggregate the results using the Pandas Framework. 
# For example, one CSV can have all employees' details, and 
# another CSV can have monthly performance for each employee. 
# The final result will be the employee and their average performance

import pandas as pd

csv1=input('Enter the first csv path:\n') #getting details csv path
csv2=input('Enter the second csv path:\n')#getting performance csv path

details=pd.read_csv(csv1) #read the csv's
performance=pd.read_csv(csv2)

group=performance.groupby('id') #grouping experience csv by emp id for calculate average

avg_performance=pd.Series(group['performance'].mean(),name="Average_performance") #calculating average performance

final_merge=pd.merge(details,avg_performance.reset_index())  

# final_merge=pd.concat([details,avg_performance.reset_index()],axis=1,join='inner')

print("\nFinal output with avgerage performance per person:\n(All rating are calculate out off 10)")

print(final_merge[['Name','Average_performance']])
