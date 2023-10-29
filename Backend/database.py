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

try:
    # execute sql statements


    curr.execute("INSERT INTO cars (price,photos,issold,description,engine,country,year,name,brand,bodytype) VALUES('78500','https://rmcmiami.com/wp-content/uploads/2023/07/E3A2837.jpg','false','NICE CAR4','Strong4','Germany','1994','E500 Limited W124','Mercedes','Sedan');")
    curr.execute("INSERT INTO cars (price,photos,issold,description,engine,country,year,name,brand,bodytype) VALUES('78500','https://rmcmiami.com/wp-content/uploads/2022/08/DSC_9986-scaled.jpg','false','NICE CAR5','Strong5','Japan','1997','RX7 FD3S','Mazda','Coupe');")
    curr.execute("INSERT INTO cars (price,photos,issold,description,engine,country,year,name,brand,bodytype) VALUES('130000','https://rmcmiami.com/wp-content/uploads/2022/12/DSC_2906-1-scaled.jpg','false','NICE CAR6','Strong6','Italy','1996','F355 Berlinetta','Ferrari','Coupe');")

    data = curr.fetchall()
    print(type(data))
    print(data)

except(Exception, psycopg2.Error) as error:
    print(error)




connection.commit() # save changes made
connection.close() # close the connection pls
curr.close() # close the cursor as well

# Create customer table
# curr.execute("CREATE TABLE IF NOT EXISTS Customer (customerid serial PRIMARY KEY, name varchar, email varchar, password varchar, phonenumber varchar);")
# Insert customer
# curr.execute("INSERT INTO customer (name, email, password, phonenumber) VALUES('Conor','conor@test.com','pass','7181112222');")
# Create cars table
# CREATE TABLE cars (carid serial PRIMARY KEY, price decimal(10,2), photos text, issold boolean, description text, engine varchar, country varchar, year int, name varchar, brand varchar, bodytype varchar);

