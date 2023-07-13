import PyPDF2
import base64


with open("janpanese.txt",'r',encoding='utf-8') as pdf:
    content=pdf.read()
    encoded_data=content.encode('utf-8')
    # print(encoded_data)

with open("japan_output.txt",'w',encoding='utf-16') as cf:
    decoded_data=encoded_data.decode('utf-8')
    # print(decoded_data)
    cf.write(decoded_data)
    
with open("janpanese.txt",encoding='utf-8') as cf:
    c1=cf.read()
with open("japan_output.txt",encoding='utf-16') as df:
    c2=df.read()
        
if c1==c2:
    print("both files have same data")
    # print(c1,'\n\n',c2)