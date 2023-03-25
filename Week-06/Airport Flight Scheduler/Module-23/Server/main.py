# Even Driven Archetecture:
import glob
import shutil
import os
import zipfile
source_path = '../Source/*'
destination_path = '../Destination/'
zip_filename = 'convert_file.zip'


postfix = [1,2,3]

source_object = glob.glob(source_path)
# print(source_object)
for source_file in source_object:
    _,execute = os.path.splitext(source_file)
    if execute == '.txt':
        object_path = source_object[0].replace('\\','/')
        shutil.copy(object_path,'.')

        object_name = object_path.split('/')[-1].split('.')
        # print(type(object_name))
        print(object_name)

        prefix = object_name[0]
        postfix2 = object_name[1]
        with zipfile.ZipFile(zip_filename, 'w') as zip_file:
            for item in range(1, len(postfix) + 1):
                num_file = item * 10
                filename = f'{prefix}_{item}.{postfix2}'
                with open(object_path, 'r') as Rfile:
                    lines = Rfile.readlines()[:num_file]
                with open(filename, 'w') as Wfile:
                    Wfile.writelines(lines)
                zip_file.write(filename)

        shutil.move(zip_filename, f'{destination_path}{zip_filename}')
        with zipfile.ZipFile(f'{destination_path}{zip_filename}', 'r') as zip_file:
            zip_file.extractall(destination_path)

    elif execute == '.py':
        os.system(f'python {source_file}')
        

os.remove(object_path)
os.remove(object_path.split('/')[-1])
