from flask import Flask
from flask import request
from flask_cors import CORS

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

app = Flask(__name__)
CORS(app)

# This does magic and allows the frontend to fetch
#cors = CORS(app, resources={r"/hello" : {"origins" : "*"}})

@app.get("/")
def home():
    print("Server Up")
    return "Server up"

# @app.route("/hello") # localhost:5000/hello
# def hello_world():
#     print("Hello World")
#     greeting = {"Hello" : "World"}
#     return greeting

@app.route("/hello/<int:price>/<int:min>/<int:max>/<string:body>")
def get_element_by_price(price,min,max,body):
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
        if body=="All":
            curr.execute("SELECT * FROM cars WHERE price <= %s AND year >= %s AND year <= %s;", (price,min,max))
        else:
            curr.execute("SELECT * FROM cars WHERE price <= %s AND year >= %s AND year <= %s AND bodytype = %s;", (price,min,max,body))

        data = curr.fetchall()
        print(type(data))
        print(data)
        # data_json = {
        #     "car_id" : data[0],
        #     "price" : data[1],
        #     "photos" : data[2],
        #     "issold" : data[3],
        #     "description" : data[4],
        #     "engine" : data[5],
        #     "country" : data[6],
        #     "year" : data[7],
        #     "name" : data[8],
        #     "brand" : data[9],
        #     "bodytype" : data[10]
        # }
        
    except(Exception, psycopg2.Error) as error:
        print(error)


    connection.commit() # save changes made
    connection.close() # close the connection pls
    curr.close() # close the cursor as well
    return data

@app.route("/specific/<int:id>")
def get_element_by_id(id):
    connection = psycopg2.connect(database = DB_NAME,
                            host = DB_HOST,
                            user = DB_USER,
                                password = DB_PASSWORD,
                                port = DB_PORT )


    # connect to database with cursor to access data
    curr = connection.cursor()


    try:
        # execute sql statements
        curr.execute("SELECT * FROM cars WHERE carid = %s;", (id,))

        data = curr.fetchall()
        #print(type(data))
        #print(data)
       
        
    except(Exception, psycopg2.Error) as error:
        print(error)

    connection.commit() # save changes made
    connection.close() # close the connection pls
    curr.close() # close the cursor as well
    return data

@app.route("/hello2/<string:brand>/<int:price>/<int:min>/<int:max>/<string:bodyType>")
def get_element_by_brand(brand, price,min,max,bodyType):
    
    connection = psycopg2.connect(database = DB_NAME,
                            host = DB_HOST,
                            user = DB_USER,
                                password = DB_PASSWORD,
                                port = DB_PORT )


    # connect to database with cursor to access data
    curr = connection.cursor()


    try:
        # execute sql statements
        if bodyType=='All':
            curr.execute("SELECT * FROM cars WHERE filter = %s AND price <= %s AND year >= %s AND year <= %s;", (brand, price,min,max))
        else:
            curr.execute("SELECT * FROM cars WHERE filter = %s AND price <= %s AND year >= %s AND year <= %s AND bodytype = %s;", (brand, price,min,max,bodyType))

        data = curr.fetchall()
        #print(type(data))
        #print(data)
       
        
    except(Exception, psycopg2.Error) as error:
        print(error)

    connection.commit() # save changes made
    connection.close() # close the connection pls
    curr.close() # close the cursor as well

   
    return data
    
@app.route('/inquire', methods = ['POST'])
def inquire_car():
    if(request.method == 'POST'):
        print("Got your post request to inquire about the car")

    else:
        print("Something happened in inquiry that wasn't supposed to")
    return {"Post Request" : "Recieved"}




@app.route("/bye")
def bye_world():
    print("Bye World")
    return {"Greetings" : "Bye, World"}

if __name__ == '__main__':
    app.run()


