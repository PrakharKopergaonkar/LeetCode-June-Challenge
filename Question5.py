#Question 5 Random Pick with Weight

import random
class Solution:
    def __init__(self, w: List[int]):
        wsum = 0
        self.w_sumarray = []
        for i in w:
            wsum+=i
            self.w_sumarray.append(wsum)
        self.w_sum = wsum
    def pickIndex(self) -> int:
        index = 0
        n = random.randint(0, self.w_sum-1)
        for i in range(0, len(self.w_sumarray)):
            if(n<self.w_sumarray[i]):
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()