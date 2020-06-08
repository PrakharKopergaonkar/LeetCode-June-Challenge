#Question 8 : Power of Two

import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n==1):
            return True
        
        elif(n<=0):
            return False
        else:
            m = math.log10(n)/math.log10(2)
            if(math.ceil(m) == math.floor(m)):
                return True
            return False
   