import csv

class employee:
    def __init__(self,EmployeeID,Name,Age,Gender,Country,Department,Position,Salary,Email):
        self.EmployeeID=EmployeeID
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
        self.Country=Country
        self.Department=Department
        self.Position=Position
        self.Salary=Salary
        self.Email=Email
        
csv1='employee.csv'   

lst=[]

with open(csv1) as cf:
    data=csv.DictReader(cf)
    for i in data:
        obj=employee(i['Employee ID'],i['Name'],i['Age'],i['Gender'],i['Country'],i['Department'],i['Position'],i['Salary'],i['Email'])
        lst.append(obj)
        
print("This is from list")   
for i in lst:
    print(i.EmployeeID,i.Name,i.Age,i.Gender,i.Country,i.Department,i.Position,i.Salary,i.Email)
            