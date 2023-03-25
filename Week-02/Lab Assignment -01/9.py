def replace_word(replace_with,s):
    for i in range(len(replace_with)):
        if i % 2 == 0:
            s = s.replace(replace_with[i],replace_with[i+1])
    return s

replace_with = ["chief","thief","superintendent","sweeper","married","left","tried","died"]

s = """I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia.Things have changed a lot since Jorina married me. 
A lot of girls tried to marry me."""

val = replace_word(replace_with,s)
print(val)