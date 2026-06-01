class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1 = sorted(s1)
        n1, n2 = len(s1), len(s2)
        for i in range(n2-n1+1):
            #print(list(s1)," = ",list(s2[i:i+n1]))
            if s1 == sorted(s2[i:i+n1]):
                return True
        return False