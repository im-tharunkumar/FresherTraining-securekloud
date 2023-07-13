import csv

# Provide the file path of the CSV file
file_path = 'employee.csv'

employee_dict = {}

# Read the CSV file and convert it into a dictionary

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        employee_id = row['Employee ID']
        employee_dict[employee_id] = row

# Print the details from the dictionary
for employee_id, details in employee_dict.items():
    for key, value in details.items():
        print(key + ":", value+"\n")
        