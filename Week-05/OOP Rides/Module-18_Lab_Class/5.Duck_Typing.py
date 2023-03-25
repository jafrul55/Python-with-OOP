class School:
    def __init__(self,name) -> None:
        self.schoolName = name
    def say_hello(self):
        print("hello from School")

class Teacher:
    def __init__(self,name) -> None:
        self.teachername = name
        # self.students = []
    def say_hello(self):
        print(f"Hello from teacher")

class Student:
    def __init__(self,name,obj) -> None:
        self.studentName = name
        obj.say_hello()

school = School("Nandail Road High School")
teacher = Teacher("Solaiman sir")
student = Student("Rakib",school)
student = Student("Rakib",teacher)

#Duck typing:
# we ca call an object and under 
# the object the method 
# will show a output.