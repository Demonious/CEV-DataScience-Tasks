from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
#Timestamp starts
start_time=time.time()

Base = declarative_base()
engine = create_engine('postgresql://postgres:7735@localhost:5432/postgres', echo = True)
Session = sessionmaker(bind = engine)
session = Session()

class login(Base):
    __tablename__ = 'Login'
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    password = Column(String(100), nullable=False)

class finding(Base):
    __tablename__="Finding"
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    password = Column(String(100), nullable=False)

def Generator(i):
  Personal_data_1 = []
  for i in range(i):
    fake=Faker()
    Personal_data_2=[]
    Personal_data_2.append(fake.email())
    Personal_data_2.append(fake.password())
    Personal_data_1.append(Personal_data_2)
  return Personal_data_1

Base.metadata.create_all(engine)

Generator(1000)

session.commit()

#Timestamp ends
end_time=time.time()
print(end_time-start_time)
