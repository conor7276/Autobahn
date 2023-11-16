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
import re


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
    liked = []

    if not name:
        print("No name entered")
        return jsonify({"error": "No name entered"}), 400
    
    email_regex_pattern = re.compile(r"([a-zA-Z0-9_.+-]+)@[a-zA-Z0-9_.+-]+\.[a-zA-z0-9_.+-]")
    if not re.match(email_regex_pattern, email): # Check if email entered is an actual email
        print("Email does not exist or meet requirements.")
        return jsonify({"error": "Email does not exist or meet requirements."}), 400
    
    password_regex_pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')
    if not re.match(password_regex_pattern, password): # check if password has correct requirements
        return jsonify({"error": "Password must contain 8 characters and at least 1 lowercase, 1 uppercase, 1 number, and 1 special character."}), 400
    
    phone_regex_pattern = re.compile(r'^[0-9]{10}$')
    if not re.match(phone_regex_pattern, phone): #Check if phone number is 10 digits
        return jsonify({"error": "Phone number must contain 10 digits"}), 400
    
    

    curr.execute("INSERT INTO Customer (name, email, password,liked, phonenumber) VALUES(%s,%s,%s,%s,%s);",(name,email,password,liked,phone))
    print("USER CREATED")
    connection.commit() # save changes made
    connection.close() # close the connection pls
    curr.close() # close the cursor as well
    
    return 'Transformed!'


@app.route('/Like', methods=['POST'])
def like():
    connection = psycopg2.connect(
        database=DB_NAME,
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    curr = connection.cursor()

    personID = request.json.get("personID", None)
    carID = request.json.get("carID", None)

    # Check if the value already exists in the array
    curr.execute("SELECT 1 FROM Customer WHERE customerid = %s AND %s = ANY(liked);", (personID, carID))
    exists = curr.fetchone()

    if not exists:
        # If the value doesn't exist, update the array
        curr.execute("UPDATE Customer SET liked = ARRAY_APPEND(liked, %s) WHERE customerid = %s;", (carID, personID))
        connection.commit()
        print("DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    else:
        print(f"{carID} already exists in the liked array for customer {personID}")

    connection.close()
    curr.close()
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

    # check if email exists first
    curr.execute("SELECT * FROM Customer WHERE email = %s;", (email,))
    data = curr.fetchall()

    # If no email return error
    if len(data) == 0:
        return jsonify({"error": "User not found"}), 400
    
    # If there is an email found check if password is correct
    curr.execute("SELECT * FROM Customer WHERE email = %s AND password = %s;", (email,password))
    data = curr.fetchall()
    print(data)
    
    
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

@app.route("/getDataLiked/<int:id>")
def getLiked(id):
    connection = psycopg2.connect(database = DB_NAME,
                            host = DB_HOST,
                            user = DB_USER,
                                password = DB_PASSWORD,
                                port = DB_PORT )
    curr = connection.cursor()
    
    curr.execute("SELECT liked FROM Customer WHERE customerid = %s;", (id,))
    data = curr.fetchall()
    print(type(data))
    print(data)
    connection.commit() # save changes made
    connection.close() # close the connection pls
    curr.close() # close the cursor as well
    return data







@app.route("/hello/<int:price>/<int:min>/<int:max>/<string:body>/<int:miles>")
def get_element_by_price(price,min,max,body,miles):
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
            curr.execute("SELECT * FROM cars WHERE price <= %s AND year >= %s AND year <= %s AND miles <= %s;", (price,min,max,miles))
        else:
            curr.execute("SELECT * FROM cars WHERE price <= %s AND year >= %s AND year <= %s AND bodytype = %s AND miles <= %s;", (price,min,max,body,miles))

        data = curr.fetchall()
        print(type(data))
        #print(data)
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






@app.route("/specifics", methods=["GET"])
def get_elements_by_ids():
    connection = None

    try:
        # Retrieve the comma-separated string of car IDs from the request args
        car_ids_str = request.args.get("car_ids", "")
        
        if not car_ids_str:
            return "No car IDs provided in the request."

        # Convert the comma-separated string to a list of integers
        car_ids = list(map(int, car_ids_str.split(',')))

        connection = psycopg2.connect(
            database=DB_NAME,
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )

        # Connect to the database with a cursor to access data
        curr = connection.cursor()

        # Use a parameterized query with the IN clause to fetch data for multiple car IDs
        curr.execute("SELECT * FROM cars WHERE carid IN %s;", (tuple(car_ids),))

        data = curr.fetchall()

    except Exception as error:
        print("Error:", error)
        data = []

    finally:
        if connection:
            connection.commit()
            connection.close()
            curr.close()

    return jsonify(data)
















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