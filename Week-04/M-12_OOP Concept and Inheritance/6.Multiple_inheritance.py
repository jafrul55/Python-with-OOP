class School:
    def __init__(self,name):
        self.school_name = name
        print('School init called')

class Grade:
    def __init__(self,grade_name):
        self.grade_name = grade_name
        print('Grade Class init called')

class SportsTeam:
    def __init__(self,sport_name):
        self.sport_name = sport_name
        self.team = []

    def add_player(self,player_name):
        self.team.append(player_name)

#Multiple Inheritance:
class Student(School,Grade,SportsTeam):
    def __init__(self, name, grade_name, school_name,sports_name):
        self.name = name
        print('Student init called')
        #you can use here 'super()' or call by class name
        Grade.__init__(self,grade_name)
        School.__init__(self,school_name)
        SportsTeam.__init__(self,sports_name)

anata_j = Student('AJ','MBA','UK School','Cricket')

print(anata_j.name)
print(anata_j.grade_name)
print(anata_j.school_name)
print(anata_j.sport_name)
print(anata_j.add_player('Borsha'))
print(anata_j.add_player('Sagor'))
print(anata_j.team)


