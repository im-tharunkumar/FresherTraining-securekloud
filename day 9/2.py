import base64

text = "Hello, 世界!"  # Unicode text

# Encode the text in UTF-8
encoded_data = text.encode('utf-8')
print(encoded_data.hex())
print(encoded_data)  # b'Hello, \xe4\xb8\x96\xe7\x95\x8c!'

# Decode the UTF-8 encoded data
decoded_text = encoded_data.decode('utf-8')
print(decoded_text)  # Hello, 世界!

text = "Hello, 世界!"  # Unicode text

# Encode the text in UTF-16
encoded_data = text.encode('utf-16')
print(encoded_data)  # b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00\xe4\x00\xb8\x00\x96\x00\xe7\x00\x95\x00\x8c\x00!\x00'

# Decode the UTF-16 encoded data
decoded_text = encoded_data.decode('utf-16')
print(decoded_text)  # Hello, 世界!

text = "Hello, 世界!"  # Unicode text

# Encode the text in UTF-32
encoded_data = text.encode('utf-32')
print(encoded_data)  # b'\xff\xfe\x00\x00H\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00,\x00\x00\x00 \x00\x00\x00\xe4\x00\x00\x00\xb8\x00\x00\x00\x96\x00\x00\x00\xe7\x00\x00\x00\x95\x00\x00\x00\x8c\x00\x00\x00!\x00\x00\x00'

# Decode the UTF-32 encoded data
decoded_text = encoded_data.decode('utf-32')
print(decoded_text)  # Hello, 世界!

text = "Hello, 世界!"  # Unicode text

# Encode the text in UTF-8 with BOM
encoded_data = text.encode('utf-8-sig')
print(encoded_data)  # b'\xef\xbb\xbfHello, \xe4\xb8\x96\xe7\x95\x8c!'

# Decode the UTF-8 BOM encoded data
decoded_text = encoded_data.decode('utf-8-sig')
print(decoded_text)  # Hello, 世界!
