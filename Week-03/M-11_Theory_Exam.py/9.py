class Two_Variable:
    def __init__(self,X,n):
        self.X = X
        self.n = n
    
    def sum(self):
        sum = self.X + self.n
        return sum
    def pow(self):
        Exp = self.X ** self.n
        return Exp
    
v1,v2 = map(int,input("Enter Two Value: ").split())

val = Two_Variable(v1,v2)

sum = val.sum()
pow = val.pow()

print(sum)
print(pow)