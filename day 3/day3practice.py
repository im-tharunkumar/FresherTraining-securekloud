import pandas as pd
import numpy as np

# z=['a','b','c','d','e']
# a=pd.Series(z)
# print(a)

# z={'x':0,'y':1,'z':2}
# a=pd.Series(z)
# print(a)

# z=pd.Series(4,index=[0,1,2,3])
# print(z)

# print(z.dtype)
# print(z.shape)
# print(z.ndim)
# print(z.nbytes)
# print(z.size)
# print(z.empty)
# print(z.hasnans)

# df=pd.read_csv("username.csv")
# print(df)

# data={
#     'id':[1,2,3,4],
#     'Name':['tharun','ragul','hariharan','tamil']
# }

# df=pd.DataFrame(data)
# print(df)

# employee_detail={
#     'Name':['Tharun','Ragul','raj kumar'],
#     'age':[22,20,21],
#     'Address':['Chennai','cudalore','kumbakonam']
# }

# df=pd.DataFrame(employee_detail, columns=['Name','age','Address'])
# df.to_csv('employee.csv',index=False)
# df

# pf=pd.read_csv('employee.csv')
# print(pf)

# experience={
#     'Name':['Tharun','Ragul','raj kumar'],
#     'Experience':[1,2,3]
# }

# df=pd.DataFrame(experience,columns=['Name','Experience'])
# df.to_csv('experience.csv',index=False)

# cf=pd.read_csv('experience.csv')
# print(cf)

# detail=pd.DataFrame(pd.read_csv('employee.csv'))
# exp=pd.DataFrame(pd.read_csv('experience.csv'))

# mer=pd.merge(detail,exp,validate='1:1')
# mer.to_csv('merge.csv',index=False)

# data={
    
#     'Name':['Tharun','ragul','raj kumar'],
#     'jan':[4,2,3],
#     'feb':[2,2,2],
#     'mar':[3,3,2]
    
# }

# per=pd.DataFrame(data)
# grp=per.groupby('Name')
# print(grp['jan','feb'].agg(np.mean))

csv1=pd.DataFrame(pd.read_csv('employee.csv'))
csv2=pd.DataFrame(pd.read_csv("performance.csv"))


grp=csv2.groupby('id')
avg_res=grp['performance'].mean()
final=pd.concat([csv1,avg_res.reset_index()],axis=1)
print(final)