def replace_comma_with_space(text):
    output = ""
    for word in text:
        if word == ",":
            output += " "
        else:
            output += word
    return output

s = "I,have,been,practising,python,since,the course,started"

output = replace_comma_with_space(s)
print(output)

