from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"
    id = Column("id", Integer, primary_key=True)
    name = Column("firstname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, id, name, gender, age):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return self.name

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    person1 = Person(1, "Mike Smith", 'M', 35)
    person2 = Person(2, "Adam Smith", 'M', 35)
    person3 = Person(3, "Jon Snow", 'M', 23)
    person4 = Person(4, "Bruce Wayne", 'M', 40)
    person5 = Person(5, "Lil Wayne", 'M', 40)
    # session.add(person2)
    # session.add(person3)
    session.add(person5)
    session.commit()
