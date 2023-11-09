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

    curr.execute("DROP TABLE cars;")
    curr.execute("CREATE TABLE cars (carid serial PRIMARY KEY, price float, photos text[], issold boolean, description text, engine varchar, country varchar, year int, name varchar, brand varchar, bodytype varchar, filter varchar, miles int);")
    #curr.execute("DELETE FROM cars;")
  
    inventory_file = open("inventory.json")
    data = json.loads(inventory_file.read())

    for car in data:

        print(car["name"])
        curr.execute("""INSERT INTO cars (price,photos,issold,description,engine,country,year,name,brand,bodytype,filter,miles)
                      VALUES (
                        %(price)s,
                        %(photos)s,
                        %(issold)s,
                        %(description)s,
                        %(engine)s,
                        %(country)s,
                        %(year)s,
                        %(name)s,
                        %(brand)s,
                        %(bodytype)s,
                        %(filter)s,
                        %(miles)s
                      );""",
                      {'price' : car['price'],
                       'photos' : car['photos'],
                       'issold' : car['issold'],
                       'description' : car['description'],
                       'engine' :  car['engine'], 
                       'country' : car['country'], 
                       'year' :  car['year'], 
                       'name' :  car['name'], 
                       'brand' : car['brand'], 
                       'bodytype' : car['bodytype'], 
                       'filter' :  car['filter'],
                       'miles' : car['miles']
                        })

    data = curr.fetchall()
    #print(data)
    
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
    #print(json_data)
    

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

