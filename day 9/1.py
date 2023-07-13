

with open("sample1.txt",'r') as cf:
    content = cf.read()
    
    encoded_data=content.encode('utf-8')
    
    print("Encoding done sucessfully")
    
with open("encoded1.txt",'w') as df:
    decoded_file=encoded_data.decode('utf-8')
    print("decoding done\nwriting content into another file:")
    df.write(decoded_file)
    
with open("sample1.txt",'r') as cf:
    c1=cf.read()
    with open("encoded1.txt") as df:
        c2=df.read()
        
if c1==c2:
    print("both files have same data")