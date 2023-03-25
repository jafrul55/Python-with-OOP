#Multiple Inheritance And MRO(Method Resulotion order):
# class School:
#     def __init__(self,name) -> None:
#         self.schoolName = name

#     def __repr__(self) -> str:
#         return f"School({self.schoolName})"

# class Teacher:
#     def __init__(self,name) -> None:
#         self.teacherName = name
#     def __repr__(self) -> str:
#         return f"Teacher({self.teacherName})"

# class Student(Teacher,School):

#     def __init__(self,name,teacherName,schoolName) -> None:
#         # Teacher.__init__(self,teacherName)
#         # School.__init__(self,schoolName)
#         #if i call to super then first parent class first
#         super().__init__(teacherName)
#         # super().__init__(schoolName)
#         self.studentName = name

#     def __repr__(self) -> str:
#         return f"Student({self.studentName})"

# student = Student("Jafrul","Rohim","KG School")
# print(student.teacherName)

#MRO:
class School:
    def __init__(self,name) -> None:
        self.schoolName = name

    def say_name(self):
        print(f"Hello I am {self.schoolName}")

    def __repr__(self) -> str:
        return f"School({self.schoolName})"

class Teacher:
    def __init__(self,name) -> None:
        self.teacherName = name

    def say_name(self):
        print(f"Hello I am {self.teacherName}")
    def __repr__(self) -> str:
        return f"Teacher({self.teacherName})"

class Student(School,Teacher):

    def __init__(self,name,teacherName,schoolName) -> None:
        Teacher.__init__(self,teacherName)
        School.__init__(self,schoolName)
        self.studentName = name

    # def say_name(self):
    #     print(f"Hello I am {self.studentName}")

    def __repr__(self) -> str:
        return f"Student({self.studentName})"

student = Student("Jafrul","Rohim","KG School")
student.say_name()

# Method Resulotion order:
# 1.jodi parent ar kacha method take tahole order wise ja aga takba taka print korba
# 2.jodi nijar modda method taka ta hole satakai print korba
