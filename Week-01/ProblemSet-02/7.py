# Two pointer Technique to check palindrom:
N = input('Enter Value: ')

leftSide = 0
rightSide = len(N)-1
while leftSide<rightSide:
    if(N[leftSide] != N[rightSide]):
        print(False)
        break
    leftSide += 1
    rightSide -= 1
else:
    print(True)