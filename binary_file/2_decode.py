data = b'hello world'
print(data)
print(type(data))

r = data.decode('utf-8')
print(r)


s = "[1, 2, 3]"
r = s.encode("ASCII")
print(r)


# String is a sequence of unicode characters
# Bytes are raw 8-bit values
