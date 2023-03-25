class Subset:
    def __init__(self,arr):
        self.arr = arr
        self.result = []

    def Subset_implement(self,start,subset):
        self.result.append(list(subset))
        
        for i in range(start,len(self.arr)):
            subset.append(self.arr[i])

            # Recursively call the Subset_implement function with updated start and subset
            self.Subset_implement(i+1,subset)

            # Remove the last element from the subset to build a new subset in the next iteration
            subset.pop()

    def Subset_call(self):
        # Call the generate_subsets function with start index 0 and an empty subset
        self.Subset_implement(0,[])
        return self.result

List = list(map(int,input("Input: ").split()))
Val = Subset(List)
result = Val.Subset_call()
print(result)
