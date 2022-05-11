str = "abc"
print(len(str))

str_bytes = str.encode('utf-8')
print(str_bytes)

new_str = str_bytes.decode('utf-8')
print(new_str)