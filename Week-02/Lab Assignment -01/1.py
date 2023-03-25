def  create_string(l):
    Sentence = ""  #take a empty string
    for word in l:
        Sentence += word + " "
    return Sentence

l = ["This","is","very","fantastic"]
print(create_string(l))