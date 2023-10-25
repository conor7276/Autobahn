from flask import Flask

app = Flask(__name__)

@app.route("/hello")

def hello_world():
    print("Hello World")
    return {"Greetings" : "Hello, World"}

@app.route("/bye")
def bye_world():
    print("Bye World")
    return {"Greetings" : "Bye, World"}

if __name__ == '__main__':
    app.run()
    #app.hello_world()