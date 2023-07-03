#Program which gets input from the user and writes it in a file. 
#The program needs to accept input text and file path.
import os as os

str1=input("Enter path: ") #input path as str1
str2=input("Enter text: ") #input Text as str2

if os.path.exists(str1):  #return true if file path exists
    print("File path exists and proceeding to write function")

try:
    with open(str1,"w") as f: #writing text in file
        f.write(str2)
    f.close()
except Exception as e:
    print("File not write")

try:
    with open(str1) as f: #Display the file
        print("Text from File",f.read())
        f.close()
except Exception as e:
    print("File not found")