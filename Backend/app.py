from flask import Flask
import json
from flask_cors import CORS

app = Flask(__name__)

# This does magic and allows the frontend to fetch
cors = CORS(app, resources={r"/hello" : {"origins" : "*"}})

@app.route("/hello") # localhost:5000/hello
def hello_world():
    print("Hello World")
    greeting = {"Hello" : "World"}
    return greeting

if __name__ == '__main__':
    app.run()