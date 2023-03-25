# with open('message.txt','w') as fileWrite:
#     fileWrite.write('Hi python,Whats up')

#for append again just use a
with open('message.txt','a') as fileWrite:
    fileWrite.write('\n Hi python,what')

#for read:
with open('message.txt','r') as fileRead:
    text = fileRead.read()
    print(text)