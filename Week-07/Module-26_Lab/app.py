""" My Cute API """
""" CRUD operation using flask """
from flask import Flask, request
database = {'Jafrul': '100','Alam': '200', 'Tusar': '300'}

#initialize flask app
app = Flask(__name__)

# if you use : http://127.0.0.1:5000/home then it will work
# @app.route('/home',methods = ['GET'])

@app.route('/',methods = ['GET'])
def home():
    return "Welcome to my cute web API"

#for get this site: http://127.0.0.1:5000/somthing 
@app.route('/somthing',methods = ['GET'])
def house():
    return """ “Any fool can write code that a computer can understand./n
                Good programmers write code that humans can understand.” – Martin Fowler
                “Before software can be reusable it first has to be usable.” – Ralph Johnson
                “Make it work, make it right, make it fast.” – Kent Beck" 
            """

@app.route('/getdata/',methods = ['GET'])
def get_data():
    return database

#Create and Read:
#routher
#api/adddata?name=id
# http://127.0.0.1:5000/adddata/?Alam=120
@app.route('/adddata/',methods = ['PUT'])
def add_data():
    key,value = list(request.args.items())[0]
    # database[key] = value
    # return f"{key} added"
    if key in database and database[key] == value:
        return f"{key} already exists in the database with value {value}"
    else:
         database[key] = value
         return f"{key} added successfully with value {value}"

#Delete:
#api/deletedata?user=name
@app.route('/deletedata/',methods = ['DELETE'])
def delete_data():
    _,value = list(request.args.items())[0]
    if value not in database:
        return f"{value} does not exist in the database"
    else:
        database.pop(value)
        return f"{value} deleted successfully"

if __name__ == '__main__':
    #to handel error:
    # app.run(host = '0.0.0.0',post=105)
    app.run()