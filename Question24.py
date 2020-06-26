# Question 24 : Unique Binary Search Trees
class Solution:
    def numTrees(self, n: int) -> int:
        dp_list = [0 for i in range(0,n+1)]
        dp_list[0] = 1
        for i in range(1,n+1):
            for j in range(1,i+1):
                left = j-1
                right = i-j
                dp_list[i]+=dp_list[left]*dp_list[right]
        return dp_list[len(dp_list)-1]