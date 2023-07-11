
# print("---------------merge of two files---------------\n")
# file1=input("Enter file 1 path:\n")
# file2=input("Enter file 2 path:\n")

# with open("Merged.txt",'a',newline='\n') as mf:
#     for file in (file1,file2):
#         with open(file) as f:
#             content=f.read()+'\n\n'
#             mf.write(content)
# print("two files merged successfully\n\n")

print("---------------split of two files---------------\n")
file=input("Enter file path to split:\n")

with open(file) as f:
    content=f.read().split('\n')
    for line in range(int(len(content)/2)):
        split1=content[line]
        print(split1)
    