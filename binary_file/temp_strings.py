from string import Template

message = """
My name is ${name}. I am learning ${language}
String formatting is 
"""
message = Template(message)

data = {"name": "Nabin", "language": "Python"}

r = message.substitute(data)
print(r)


a = [1, 2, 3]
b = ["Sun", "Mon", "Tues"]
for x, y in zip(a, b):
    print(x, y)


a = {"1": 2, "3": 4}
b = dict(**a, x=1)
print(b)
