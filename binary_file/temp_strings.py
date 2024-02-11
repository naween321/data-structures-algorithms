from string import Template

message = """
My name is ${name}. I am learning ${language}
String formatting is 
"""
message = Template(message)

data = {"name": "Nabin", "language": "Python"}

r = message.substitute(data)
print(r)
