# a="a".encode("utf-8")
# print(a)

a=input("Enter character:\n")
print(ord(a))

b=int(input("Enter unicode value:\n"))
print(chr(b))

# from codecs_to_hex import to_hex

txt="I am Tharun"
encoded=txt.encode("utf-8")
print(encoded.hex())

# decoded=encoded.decode("utf-8")
# print(decoded)

import base64 as b

# txt='i am tharun'
# encoded=txt.encode("utf-8")
# print(b.b64encode(encoded))

with open('sample1.txt','rb') as cf:
    content=cf.read()
    print(content)
    content=b.b64decode(content)
    
    print(content)