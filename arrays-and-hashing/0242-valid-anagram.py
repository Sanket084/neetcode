class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)  #soln 1

        #return sorted(s) == sorted(t)   # soln 2
                                         # soln 3 given below:
        # if len(s) != len(t):
        #     return False
        
        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False
        # return True
            