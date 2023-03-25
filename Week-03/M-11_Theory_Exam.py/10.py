import math
class Distance:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def compute(self):
        return math.sqrt((self.x2-self.x1)**2 + (self.y2 - self.y1)**2)
    
x1,y1,x2,y2 = map(int,input("Enter X1,Y1 and X2,Y2: ").split())

Val = Distance(x1,y1,x2,y2)
Output = Val.compute()

print("Output is = ",Output)
