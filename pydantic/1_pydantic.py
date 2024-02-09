from pydantic import BaseModel
from pydantic import ValidationError


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


p = Person(age=30, first_name="Jon", last_name="Doe")

try:
    Person(first_name="Jon")
except ValidationError as e:
    print(e.json())


# To provide optional
class Person(BaseModel):
    first_name: str = "Jane"
    last_name: str
    age: int = None

p = Person(last_name="Doe", age=30)
# print(p.model_dump())
# print(p.model_dump_json())


data = p.model_dump()
print(data)
p = Person.model_validate(data)
print(p)