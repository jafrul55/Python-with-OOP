def full_name(f_name,l_name):
    name = f'{f_name} {l_name}'
    return name

name = full_name(l_name='Jafrul',f_name='Alam')
# print(name)
# name = full_name(l_name='chowdhury',middle = 'rahman')

# def long_name (**kargs):  #key kargs
    # print(kargs)

# long_name(first = 'Dr.',last = 'Chowdhury',middle = 'Rahman')



# def name_mixed(first,last,**name_parts):
#     print(first,last,name_parts)

# name = name_mixed(first='chowdhury',last='choto',middle='major')
# print(name)


# def all_types(first,*args,**Kargs):  #hare args and kargs and normal parameter available
#     print('First: ',first)
#     print('Args: ',args)
#     print('Kargs: ',Kargs)

# all_types('abd','ddd','kik','lll','ppp',name = 'Jafrul',father='Atikul')

# If you want to print args and kargs using loop Then:
def all_types1(first,*args,**kargs):
    print(first)
    for word in args:
        print(word)

    for key,value in kargs.items():
        print(key,value)

all_types1('abd','ddd','kik','lll','ppp',name = 'Jafrul',father='Atikul')

