weight = 40
weight_type = type(weight)
print(weight_type) #type int

price = 13.79
price_type = type(price)
print(price_type)  #type float


pen = 'Econo'
print(type(pen)) #string type

age = 45
kanamachi = True
print(type(kanamachi))

Person = 'Tita Ali'
# about_me = 'My Name is' + Person + age
about_me = f'My Name is {Person}.My age is {age}.'
# f string
print(about_me)