# def create_new_string(a,s):
#     new_string = []
#     s = s.replace(',','')
#     words = s.split()
#     words.reverse()
#     for i in a:
#         for j in words:
#             if i.lower() == j.lower():
#                 index = words.index(j)
#                 if words[index-1] not in new_string:
#                     new_string.append(words[index-1])
#     return ' '.join(new_string)

# a = ['oh', 'Emelia', 'to']

# s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."
# print(create_new_string(a,s))


def create_new_string(a,s):
    new_string = " "
    s = s.replace(',','')
    words = s.split()
    words.reverse()
    for i in a:
        for j in words:
            if i.lower() == j.lower():
                index = words.index(j)
                if words[index-1] not in new_string:
                    new_string += words[index-1] + " "
    with open('out.txt','w') as file:
        file.write(new_string)
        file.close()
     
a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."
create_new_string(a,s)


