def create_new_string(s, a):
    words = s.split()
    new_string = []
    for i in range(len(words)):
        if words[i] in a:
            for j in range(i+1, len(words)):
                if words[j] not in a:
                    new_string.append(words[j])
                else:
                    break
    new_string = ' '.join(new_string)
    print(new_string)
    with open('out.txt', 'w') as f:
        f.write(new_string)
    f.close()

a = ['oh', 'Emelia', 'to']
s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."
create_new_string(s, a)
