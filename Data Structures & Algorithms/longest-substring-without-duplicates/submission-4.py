class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxi = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]]+1)
            seen[s[r]] = r
            maxi = max(maxi, r - l + 1)

        return maxi
            

