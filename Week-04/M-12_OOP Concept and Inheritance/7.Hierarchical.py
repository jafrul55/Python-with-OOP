class Employee:
    def __init__(self,name,id,salary,position,experience):
        self.name = name
        self.id = id
        self.salary = salary
        self.position = position
        self.experience = experience


class Developer(Employee):
    def __init__(self,name,id,salary,position,tech,focus):
        
        super().__init__(name,id,salary,position)
        self.tech = tech
        self.focus = focus

class Testing(Employee):
    pass

class Seles(Employee):
    pass

class TechLead(Employee):
    def __init__(self, name, id, salary, position, team):
        self.team = team
        super().__init__(name,id,salary,position)

