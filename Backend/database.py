from dotenv import load_dotenv
import psycopg2

import os
from os.path import join, dirname
import json



dotenv_path = join(dirname(__file__),'.env')

load_dotenv(dotenv_path)

DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")



    # connect to database
connection = psycopg2.connect(database = DB_NAME,
                            host = DB_HOST,
                            user = DB_USER,
                                password = DB_PASSWORD,
                                port = DB_PORT )


# connect to database with cursor to access data
curr = connection.cursor()

print("Attempting the great SQL Creation")
try:
    # execute sql statements
    curr.execute("INSERT INTO cars (price,photos,issold,description,engine,country,year,name,brand,bodytype) VALUES('100000','https://media4.speedcafe.com/wp-content/uploads/2021/01/Porsche-911-Turbo-S-003-scaled.jpg','false','NICE CAR','Strong','Germany','2021','911 Turbo S Coupe','Porsche','Coupe');")

    data = curr.fetchall()
    print(type(data))
    print(data)

except(Exception, psycopg2.Error) as error:
    print("Machine broke gg ", error)

print("WE FUCKING DID IT")


connection.commit() # save changes made
connection.close() # close the connection pls
curr.close() # close the cursor as well

# Create customer table
# CREATE TABLE IF NOT EXISTS Customer (customerid serial PRIMARY KEY, name varchar, email varchar, password varchar, phonenumber varchar);
# Insert customer
# INSERT INTO customer (name, email, password, phonenumber) VALUES('Conor','conor@test.com','pass','7181112222');
# Create cars table
# CREATE TABLE cars (carid serial PRIMARY KEY, price decimal(10,2), photos text, issold boolean, description text, engine varchar, country varchar, year int, name varchar, brand varchar, bodytype varchar);
# 