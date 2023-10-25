from flask import Flask
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

# This does magic and allows the frontend to fetch
cors = CORS(app, resources={r"/hello" : {"origins" : "*"}})

@app.get("/")
def home():
    print("Server Up")
    return "Server up"

# @app.route("/hello") # localhost:5000/hello
# def hello_world():
#     print("Hello World")
#     greeting = {"Hello" : "World"}
#     return greeting

@app.route("/hello")
def hello_world():
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
        curr.execute("SELECT * FROM customer;")

        data = curr.fetchall()
        print(type(data))
        print(data)
        return data
    except:
        print("Machine broke gg")

    print("WE FUCKING DID IT")


    connection.commit() # save changes made
    connection.close() # close the connection pls
    curr.close() # close the cursor as well

@app.route("/bye")
def bye_world():
    print("Bye World")
    return {"Greetings" : "Bye, World"}

if __name__ == '__main__':
    app.run()


