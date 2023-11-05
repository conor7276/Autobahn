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
    # curr.execute("DELETE FROM cars;")
    #curr.execute("CREATE TABLE cars (carid serial PRIMARY KEY, price float, photos text[], issold boolean, description text, engine varchar, country varchar, year int, name varchar, brand varchar, bodytype varchar, filter varchar);")
    
    #curr.execute("INSERT INTO cars (price,photos,issold,description,engine,country,year,name,brand,bodytype,filter) VALUES('78500',ARRAY['https://rmcmiami.com/wp-content/uploads/2022/07/DSC_9193-scaled.jpg.webp','https://rmcmiami.com/wp-content/uploads/2022/07/DSC_9195-scaled.jpg.webp','https://rmcmiami.com/wp-content/uploads/2022/07/DSC_9202-scaled.jpg.webp','https://rmcmiami.com/wp-content/uploads/2022/07/DSC_9217-scaled.jpg.webp','https://rmcmiami.com/wp-content/uploads/2022/07/DSC_9220-scaled.jpg.webp','https://rmcmiami.com/wp-content/uploads/2022/07/DSC_9223-scaled.jpg.webp','https://rmcmiami.com/wp-content/uploads/2022/07/DSC_9224-scaled.jpg.webp','https://rmcmiami.com/wp-content/uploads/2022/07/DSC_9225-scaled.jpg.webp','https://rmcmiami.com/wp-content/uploads/2022/07/DSC_9226-scaled.jpg.webp','https://rmcmiami.com/wp-content/uploads/2022/07/DSC_9240-scaled.jpg.webp'],'false','NICE CAR4','Strong4','Germany','1994','E500 Limited W124','Mercedes','Sedan','Mercedes');")
    # curr.execute("INSERT INTO cars (price,photos,issold,description,engine,country,year,name,brand,bodytype,filter) VALUES('78500',ARRAY['https://rmcmiami.com/wp-content/uploads/2022/08/DSC_9986-scaled.jpg'],'false','NICE CAR5','Strong5','Japan','1997','RX7 FD3S','Mazda','Coupe','Special');")
    # curr.execute("INSERT INTO cars (price,photos,issold,description,engine,country,year,name,brand,bodytype,filter) VALUES('130000',ARRAY['https://rmcmiami.com/wp-content/uploads/2022/12/DSC_2906-1-scaled.jpg'],'false','NICE CAR6','Strong6','Italy','1996','F355 Berlinetta','Ferrari','Coupe','Foreigners');")
    curr.execute("INSERT INTO cars (price,photos,issold,description,engine,country,year,name,brand,bodytype,filter) VALUES('200000',ARRAY['https://static.cargurus.com/images/forsale/2023/09/25/20/45/2016_porsche_911-pic-3372716953071438188-1024x768.jpeg','https://static.cargurus.com/images/forsale/2023/09/25/20/45/2016_porsche_911-pic-9118996043708167974-1024x768.jpeg','https://static.cargurus.com/images/forsale/2023/09/25/20/45/2016_porsche_911-pic-292600427420951491-1024x768.jpeg','https://static.cargurus.com/images/forsale/2023/11/02/14/02/2016_porsche_911-pic-1872210323998749890-1024x768.jpeg','https://static.cargurus.com/images/forsale/2023/11/02/14/02/2016_porsche_911-pic-8615248157059783330-1024x768.jpeg','https://static.cargurus.com/images/forsale/2023/09/25/20/45/2016_porsche_911-pic-6782416641908166509-1024x768.jpeg','https://static.cargurus.com/images/forsale/2023/11/02/14/02/2016_porsche_911-pic-4874578565966485695-1024x768.jpeg','https://static.cargurus.com/images/forsale/2023/09/25/20/45/2016_porsche_911-pic-2830876654065179943-1024x768.jpeg','https://static.cargurus.com/images/forsale/2023/11/02/14/02/2016_porsche_911-pic-5095890299284408736-1024x768.jpeg','https://cdn.cnn.com/cnnnext/dam/assets/190910153058-06-sept-11-timeline-2-full-169.jpg'],'false','The Porsche 911 GT3 RS Coupe is a high-performance sports car known for its speed, precision, and racing-inspired design. With a lightweight build, aerodynamic features, and a powerful engine, it delivers thrilling performance on both the track and the road. Inside, it offers a racing-inspired interior with advanced technology and precise handling. It`s a dream car for those seeking the ultimate combination of style and performance.','500 hp 4L H6','Germany','2016','Porsche 911 GT3 RS Coupe RWD','Porsche','Coupe','Porsche');")
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

