from flask import Flask
from flask import request,jsonify
from flask_cors import CORS
from flask import render_template
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import psycopg2
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager


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
app.config["JWT_SECRET_KEY"] = "please-remember-to-change-me"
jwt = JWTManager(app)
# This does magic and allows the frontend to fetch
#cors = CORS(app, resources={r"/hello" : {"origins" : "*"}})
#//////////////////////////////////
@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    
    connection = psycopg2.connect(database = DB_NAME,
                            host = DB_HOST,
                            user = DB_USER,
                                password = DB_PASSWORD,
                                port = DB_PORT )
    curr = connection.cursor()
    name=request.json.get("name",None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    phone=request.json.get("phone",None)
    curr.execute("INSERT INTO Customer (name, email, password, phonenumber) VALUES(%s,%s,%s,%s);",(name,email,password,phone))
    print("USER CREATED")
    connection.commit() # save changes made
    connection.close() # close the connection pls
    curr.close() # close the cursor as well
    return 'Transformed!'






@app.route('/token', methods=["POST"])
def create_token():
    connection = psycopg2.connect(database = DB_NAME,
                            host = DB_HOST,
                            user = DB_USER,
                                password = DB_PASSWORD,
                                port = DB_PORT )


    # connect to database with cursor to access data
    curr = connection.cursor()
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    curr.execute("SELECT * FROM Customer WHERE email = %s AND password = %s;", (email,password))
    data = curr.fetchall()
    print(data)
    
    if len(data) == 0:
        print("No Good")
        return {"msg": "Wrong email or password"}, 401
    user_id = data[0] 
    access_token = create_access_token(identity=email)
    print("guuuuuuud")
    response = {"access_token":access_token , "user_id": user_id}
    connection.commit() # save changes made
    connection.close() # close the connection pls
    curr.close() # close the cursor as well
    return response

@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response
    


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

@app.route("/hello2/<string:brand>/<int:price>/<int:min>/<int:max>/<string:bodyType>/<int:miles>")
def get_element_by_brand(brand, price,min,max,bodyType,miles):
    
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
            curr.execute("SELECT * FROM cars WHERE filter = %s AND price <= %s AND year >= %s AND year <= %s AND miles <= %s;", (brand, price,min,max,miles))
        else:
            curr.execute("SELECT * FROM cars WHERE filter = %s AND price <= %s AND year >= %s AND year <= %s AND bodytype = %s AND miles <= %s;", (brand, price,min,max,bodyType,miles))

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


