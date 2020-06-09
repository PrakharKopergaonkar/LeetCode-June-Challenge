#Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(s=="") : return True
        if(t=="") : return False
        for i in s:
            if(i in t):
                t = t[t.index(i)+1::]
            else:
                return False
        return True
                