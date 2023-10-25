from flask import Flask
from flask_cors import CORS


app = Flask(__name__)

<<<<<<< HEAD
@app.route("/hello")

=======
# This does magic and allows the frontend to fetch
cors = CORS(app, resources={r"/hello" : {"origins" : "*"}})

@app.get("/")
def home():
    print("Server Up")
    return "Server up"

@app.route("/hello") # localhost:5000/hello
>>>>>>> dce602a2329813432fce2ce90d32aee1a1447def
def hello_world():
    print("Hello World")
    greeting = {"Hello" : "World"}
    return greeting

@app.route("/bye")
def bye_world():
    print("Bye World")
    return {"Greetings" : "Bye, World"}

if __name__ == '__main__':
    app.run()


