with open("center.txt",'r') as file:
    lines = file.readlines()
    max_len = max(len(line.strip()) for line in lines)
    for line in lines:
        Cent = line.strip().center(max_len)
        print(Cent)