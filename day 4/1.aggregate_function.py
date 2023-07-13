import pandas as pd

df=pd.read_csv('1.csv')
# print(df)

# print(df['Name'])

salary_mean=df['Salary'].mean()
print('mean of salary:\n',salary_mean)

salary_median=df['Salary'].median()
print('median of salary:\n',salary_median)

salary_sum=df['Salary'].sum()
print('sum of salary:\n',salary_sum)

# print(df.describe())

print('Total no. of people:\t',df['Name'].count())

Edu_count=df['Education'].value_counts()
print("Degree wise count:\n",Edu_count)

Occ_count=df['Occupation'].value_counts()
print("Occupation wise count:\n",Occ_count)

socialmedia=df['Social Media'].value_counts()
print("Social media wise count\n",socialmedia)

socialmedia=df['Social Media'].value_counts(normalize=True)
print("Percentage of media\n",socialmedia)

country=df['Country'].value_counts()
print("print count count\n",country)

country_group=df.groupby(['Country'])

a=country_group.get_group('USA')
print("Group by USA\n",a)

filt=df['Social Media'] == 'LinkedIn'
b=df.loc[filt]
print("Filtered LinkedIn user\n",b )

filter=df['Social Media'] == 'LinkedIn'     #filtering by col
c=df.loc[filter]['Country'].value_counts()
print("printing linkin user country wise\n",c)

filter=df['Country'] == 'USA'  
d=df.loc[filter]['Social Media'].value_counts()   #Here we have to write filter for each country
print("Printing USA social media",d)

coun_wise_social_count=country_group['Social Media'].value_counts() #this brings all country wise social media count
print('country wise social media count\n',coun_wise_social_count)

coun_wise_social_count=country_group['Social Media'].value_counts().loc['USA']
print("Alternate for filter\n",coun_wise_social_count) #filter and this method are same we have to write each time

country_wise_salary_mean=country_group['Salary'].mean()
print("country wise salary mean\n",country_wise_salary_mean)

country_wise_salary_mean=country_group['Salary'].mean().loc['UK']
print("Specific country salary mean",country_wise_salary_mean) # include filter

agg_fun=country_group['Salary'].agg(['median','mean'])
print("Using agg\n",agg_fun)

agg_fun=country_group['Salary'].agg(['median','mean']).loc['Canada']
print("filter with agg for canada \n",agg_fun) #include filter with agg fun

contains=df['Salary'].isnull()
null_contains=df.loc[contains]
print("Printing where salary is null",null_contains)

unique=df['Name'].unique()
print("Printing unique name\n",unique)

zz=df['State'].str.contains("California")
ss=df.loc[zz]
print("Filtered where state is califonia\n",ss)

zz=df['State'].str.contains("California")
ss=df.loc[~zz]
print("Printing state other than califonia\n",ss)

