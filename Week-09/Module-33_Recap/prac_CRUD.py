from flask import Flask,jsonify,request

app = Flask(__name__)
Students = [{'id':1,'name':'Jafrul'},{'id':2,'name':'Alam'},{'id':3,'name':'Tusar'}]

@app.route('/')
def home():
    return jsonify(Students)


@app.route('/add',methods = ['POST'])
def add():
    Students.append(request.get_json())
    return "Your adding successfully done"

@app.route('/update',methods = ['PUT'])
def update():
    for student in Students:
        if student.get('id') == request.get_json().get('id'):
            student.update(request.get_json())
            break
    return "Your updating already done"
    
@app.route('/delete',methods = ['DELETE'])
def delete():
    for student in Students:
        if student.get('id') == request.get_json().get('id'):
            Students.remove(student)
            break
    return "Your deleting already done"

app.run(debug=True)