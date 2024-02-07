from main import session, Person


results = session.query(Person).all()
print(results)

results = list(session.query(Person).filter(Person.id == 1))
print(results)

# session.query(Person).filter(Person.id == 5).delete()
# session.commit()
# print("Delete Success!!")

session.query(Person).filter(Person.id == 1).update(dict(name="Rohan"))
session.commit()
print("Update Successful !!")


