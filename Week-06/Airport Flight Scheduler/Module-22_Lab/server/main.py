""" Object process """
# Event-Driven archetecture:

import glob
import shutil  #to copy
import os

source_path = '../source/*'

destination_path = "../destination/"
postfix = [1,2,3]

#Now it's automatically will work: if i crate a new txt file in source file
while True:
    source_object = glob.glob(source_path)
    # print(source_object)
    if(len(source_object) > 0):

        object_path = source_object[0].replace('\\','/')
        # print(object_path)

        shutil.copy(object_path, '.') #copy file

        object_name = object_path.split('/')[-1].split('.')

        # print(object_name)
        # print(type(object_name))

        prefix = object_name[0]
        postfix2 = object_name[1]

        # print(prefix)
        # print(prefix2)


        for item in range(len(postfix)):
            filename = prefix + '_' + str(item) + '.' + postfix2
            print(filename)

            # shutil.copy(object_path,filename)

            #copy file: to send in destination
            shutil.copy(object_path,f"{destination_path}/{filename}")

        os.remove(object_path)
        os.remove((object_path.split('/')[-1]))
