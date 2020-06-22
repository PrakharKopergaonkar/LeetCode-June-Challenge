#Question 22: Single Number II
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = dict()
        for i in nums:
            if(i in a):
                if(a[i]==2):
                    del a[i]
                else:
                    a[i]+=1
            else:
                a[i] = 1
        
        return list(a.keys())[0]
    