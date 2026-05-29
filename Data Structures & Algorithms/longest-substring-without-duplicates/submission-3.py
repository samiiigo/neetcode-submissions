class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        seen, maxi = set(s[0]), 1
        l, r = 0, 1
        
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                maxi = max(maxi,r-l+1)
                r+=1
            else:
                l +=1
                seen = set(s[l])
                r = l+1
        return maxi
            

