def clean_string(text):
    output = "".join(v for v in text if v.isalpha())
    return output

s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)