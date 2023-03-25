""" Encrypt the following code sothat no one can get your strategy """
data = "firebaby"

shift = 4

output = ''

for character in data:
    output += chr((ord(character)+shift-97) % 26 + 97)

print(output)