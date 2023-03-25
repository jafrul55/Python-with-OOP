class Element:
    def __init__(self,numbers,target):
        self.numbers = numbers
        self.target = target

    def find_pair(self):
        for i in range(len(self.numbers)):
            for j in range(i+1,len(self.numbers)):
                if self.numbers[i] + self.numbers[j] == self.target:
                    return (i+1,j+1)
        return None

Numbers = [10,20,10,40,50,60,70]
target = 50

val = Element(Numbers,target)
outcome = val.find_pair()
# print(outcome)
if outcome:
    print("Output = "f"{outcome[0]},{outcome[1]}")
else:
    print("No pair found")
