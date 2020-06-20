#   Question 20 : Permutation Sequence
import math
class Solution:   
    def __init__(self):
        self.string = ""
    def generatepermute(self,numbers,count,string,k):
        for i in numbers:
            if(str(i) not in string):
                digits = len(numbers)-len(string)-1
                if(digits==0):
                    self.string=string+str(i)
                    return True
                if(count+math.factorial(digits)<k):
                    count+=math.factorial(digits)
                elif(count+math.factorial(digits)>=k):
                    a = self.generatepermute(numbers,count,string+str(i),k)
                    if(a==True):
                        return True
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [i for i in range(1, n+1)]
        count = 0
        self.generatepermute(numbers,count,"",k)
        return self.string
        