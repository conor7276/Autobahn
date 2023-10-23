from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import psycopg2

import os
import json

load_dotenv()


app = Flask(__name__)

url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

# This does magic and allows the frontend to fetch
cors = CORS(app, resources={r"/hello" : {"origins" : "*"}})

@app.get("/")
def home():
    print("Server Up")
    return "Server up"

@app.route("/hello") # localhost:5000/hello
def hello_world():
    print("Hello World")
    greeting = {"Hello" : "World"}
    return greeting

if __name__ == '__main__':
    app.run()