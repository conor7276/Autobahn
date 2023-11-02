from dotenv import load_dotenv
import psycopg2
import json
import os
from os.path import join, dirname


from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

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
    # curr.execute("DROP TABLE cars;")
    # curr.execute("CREATE TABLE cars (carid serial PRIMARY KEY, price float, photos text[], issold boolean, description text, engine varchar, country varchar, year int, name varchar, brand varchar, bodytype varchar, filter varchar);")
    
    # curr.execute("INSERT INTO cars (price,photos,issold,description,engine,country,year,name,brand,bodytype,filter) VALUES('78500',ARRAY['https://rmcmiami.com/wp-content/uploads/2023/07/E3A2837.jpg','http://masbukti.com/manufacturers/mercedes-benz/mercedes-benz-e-class/1994-mercedes-benz-e-class-coupe/1994-mercedes-benz-e-class-coupe-3.jpg'],'false','NICE CAR4','Strong4','Germany','1994','E500 Limited W124','Mercedes','Sedan','Mercedes');")
    # curr.execute("INSERT INTO cars (price,photos,issold,description,engine,country,year,name,brand,bodytype,filter) VALUES('78500',ARRAY['https://rmcmiami.com/wp-content/uploads/2022/08/DSC_9986-scaled.jpg'],'false','NICE CAR5','Strong5','Japan','1997','RX7 FD3S','Mazda','Coupe','Special');")
    # curr.execute("INSERT INTO cars (price,photos,issold,description,engine,country,year,name,brand,bodytype,filter) VALUES('130000',ARRAY['https://rmcmiami.com/wp-content/uploads/2022/12/DSC_2906-1-scaled.jpg'],'false','NICE CAR6','Strong6','Italy','1996','F355 Berlinetta','Ferrari','Coupe','Foreigners');")

    data = curr.fetchall()
    print(type(data))
    
    #print(json.dumps(data, cls=DecimalEncoder))
    categorized_data_list = []
    for row in data:
        categorized_data = {
            "car_id": row[0],
            "price": row[1],
            "photo_url": row[2],
            "is_available": row[3],
            "description": row[4],
            "condition": row[5],
            "origin": row[6],
            "year": row[7],
            "model": row[8],
            "make": row[9],
            "body_type": row[10]
        }
        categorized_data_list.append(categorized_data)

    json_data = json.dumps(categorized_data_list, cls=DecimalEncoder)
    print(json_data)
    

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

