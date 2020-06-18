# Question 18 : H-Index II
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        length = len(citations)
        right = length-1
        if(len(citations)==0) : return 0
        if(len(citations)==1 and citations[0]!=0) : return 1
        if(len(citations)==1 and citations[0]==0): return 0
        while(left<=right):
            mid = int((left+right)/2)
            print(left, right, mid)
            if(citations[mid]<length-mid):
                left = mid+1
            else:
                right = mid-1
        return length-left