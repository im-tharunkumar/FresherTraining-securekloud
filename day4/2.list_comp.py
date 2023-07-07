#list for n numbers

n=int(input("Enter n:\n"))
list1=[x for x in range(1,n+1)]
print("List of n:\n",list1)

#list for n**2 
list2=[x**2 for x in range(1,n+1)]
print("List of n square:\n",list2)

#list of even number
list3=[x for x in range(1,n+1) if x%2==0]
print("List of Even numbers\n",list3)

#list of tuples
list4=[(x,y) for x in range(1,n+1) for y in range(n,1,-1) ]
print("List of tuple(x,y):\n",list4)

# Sample employee data
employees = [
    {'name': 'John', 'age': 32, 'salary': 50000},
    {'name': 'Jane', 'age': 28, 'salary': 60000},
    {'name': 'Mark', 'age': 35, 'salary': 70000},
    {'name': 'Emily', 'age': 30, 'salary': 55000},
    {'name': 'David', 'age': 40, 'salary': 80000}
]

# Calculate the total salary using lambda function
total_salary = sum(map(lambda emp: emp['salary'], employees))
print("Total Salary:", total_salary)

# Find the maximum age using lambda function
max_age = max(employees, key=lambda emp: emp['age'])['age']
print("Maximum Age:", max_age)

# Find the average salary using lambda function
avg_salary = sum(map(lambda emp: emp['salary'], employees)) / len(employees)
print("Average Salary:", avg_salary)
