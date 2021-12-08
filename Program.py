import datetime
from User import User
from Car import Car
from sqlalchemy import text
from db_cofig import local_session, create_all_entities

# create tables
create_all_entities()

# local_session.add(User(username='bob', email='bob@bob.com'))
# local_session.commit()

# add a list of users
# users_list = [User(username='rob', email='rob@rob.com'), User(username='job', email='job@job.com')]
# local_session.add_all(users_list)
# local_session.commit()
#
# # delete a user
# local_session.query(User).filter(User.id == 2).delete(synchronize_session=False)
# local_session.commit()

# print all users
users = local_session.query(User).all()
print(users)

# add cars
car1 = Car(id=1, model='Mazda', brand='Active3', year=datetime.datetime(2010, 7, 1))
car2 = Car(id=2, model='Renault', brand='Cleo', year=datetime.datetime(2018, 6, 15))
car3 = Car(id=3, model='Ford', brand='Focus', year=datetime.datetime(2016, 10, 6))
car4 = Car(id=4, model='Mazda', brand='Active3', year=datetime.datetime(2018, 12, 1))
car5 = Car(id=5, model='Mazda', brand='Portrait12', year=datetime.datetime(2022, 2, 1))

local_session.add(car1)
local_session.add(car2)
local_session.add_all([car3, car4, car5])
local_session.commit()

cars = local_session.query(Car).all()
print(cars)
