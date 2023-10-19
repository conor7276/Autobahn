from flask import Flask

app = Flask(__name__)

def hello_world():
    print("Hello World")
    return {"Greetings" : "Hello, World"}

if __name__ == '__main__':
    app.run()
    #app.hello_world()