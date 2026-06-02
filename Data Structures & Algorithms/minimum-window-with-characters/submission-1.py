class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        for i in t:
            if i not in s:
                return ""

        tcount = {}
        for i in t:
            tcount[i] = tcount.get(i, 0) +1
        
        n = len(s)
        res = ""
        for l in range(n):
            count = {}
            curr = 0

            if s[l] in t:
                for r in range(l, n):
                    count[s[r]] = count.get(s[r],0)+1
                    if count[s[r]] == tcount.get(s[r]):
                        curr += 1
                    if curr == len(tcount):
                        if len(res) == 0 or len(res)>len(s[l:r+1]):
                            res = s[l:r+1]
        return res
