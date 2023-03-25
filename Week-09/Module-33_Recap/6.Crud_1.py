#Flask CRUD Operations using Query
from flask import Flask, jsonify,request

app = Flask(__name__)

students = [{'id': 1, 'name':'rahim'},{'id': 2,'name':'korim'}]
@app.route('/')
def home():
    return jsonify(students)

#to add :
@app.route('/add',methods = ['GET','POST'])

# http://127.0.0.1:5000/add?id=value&name= name write
def add():
    students.append(request.args)
    return "Student added successfully."

#To Update:
# http://127.0.0.1:5000/update?id=1&name=Alam
@app.route('/update',methods = ['GET','PUT'])

def Update():
    print(request.args)
    for student in students:
        if str(student.get('id')) == request.args.get('id'):
            student.update(request.args)
    return "Student updated successfully."

# To Delete:
# http://127.0.0.1:5000/delete?id=2&name=korim
@app.route('/delete',methods = ['GET','DELETE'])
def delete():
    for i in range(len(students)):
        if str(students[i].get('id')) == request.args.get('id'):
            del students[i]
            break
    return "Student Deleted Successful"

app.run(debug = True)
