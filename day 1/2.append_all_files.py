#Program to read all the files in a folder and append the contents in a single file. 
#The program needs to accept the input path andoutput path as parameters
import os as os
from pathlib import Path

file_dir=Path(input("Enter Dir: "))       #Getting Directory path
file_name=input("Enter NewFile path: ")   #Getting Outputfile path

#file_path=file_dir.joinpath(file_name) ' use to create path if filename given

all_file=os.listdir(file_dir) #create list of all type of files

newfile=open(file_name,'a') # open newfile as append mode

for i in all_file:
    if i.endswith(".txt"): #filters text files only
        file1=open(i,'r')
        newfile.write(file1.read())
        newfile.write('\n')
        file1.close()

newfile.close()

with open(file_name,'r') as f:
    print('Text from new file:\n',f.read())
    file_name.close()