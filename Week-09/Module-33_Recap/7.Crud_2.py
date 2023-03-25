#Crud Operation using Flask part-2
from flask import Flask, jsonify,request

app = Flask(__name__)

students = [{'id':1, 'name':'rahim'},{'id': 2,'name':'korim'}]
@app.route('/')
def home():
    return jsonify(students)


#To Add :
@app.route('/add',methods = ['POST'])

# http://127.0.0.1:5000/add?id=value&name= name write
def add():
    students.append(request.get_json())
    print(request.get_json())
    return "Student added successfully.",200


#To Update:
# http://127.0.0.1:5000/update?id=1&name=Alam
@app.route('/update',methods = ['PUT'])

def Update():
    for student in students:
        if student.get('id') == request.get_json().get('id'):
            student.update(request.get_json())
            print("Student updated successfully.",request.get_json())
    return "Student updated successfully."


# To Delete:
# http://127.0.0.1:5000/delete?id=2&name=korim
@app.route('/delete',methods = ['DELETE'])
def delete():
    for i in range(len(students)):
        if students[i].get('id') == request.get_json().get('id'):
            del students[i]
            break
    print("Student Deleted Successful",request.get_json())
    # print(type(request.get_json().get('id')))
    return "Student Deleted Successful"

app.run(debug = True)
