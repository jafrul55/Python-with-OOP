class User:
    def __init__(self,f_name,l_name):
        self.first = f_name
        self.last = l_name
        self.email = f'{self.first}.{self.last}@user.com'
    @property 
    #use @property for work to print as property
    def full_name(self):
        return f'{self.first} {self.last}'
    
    @full_name.setter
    def full_name(self,value): #if you want to change full name
        first,last = value.split(' ')
        self.first = first
        self.last = last
        # self.first = value.split(' ')[0]
        # self.last = value.split(' ')[1]
        self.email = f'{first}.{last}@user.com'
    
    @full_name.deleter
    def full_name(self):
        del self.first
        del self.last

    def get_email(self):
        return self.email
marks = User('marks','Zuku')
print(marks.first)
print(marks.last)
print(marks.email)
print(marks.get_email()) #call as method
print(marks.full_name) #use as property
marks.full_name = 'Tom Hanks'
print(marks.full_name)
print(marks.email)
del marks.full_name
print(marks.first)
print(marks.last)