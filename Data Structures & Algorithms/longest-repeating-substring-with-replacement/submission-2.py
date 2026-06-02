class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for char in set(s):
            left = 0
            count = 0
            for right in range(len(s)):
                if s[right] != char:
                    count += 1
                while count > k:
                    if s[left] != char:
                        count -= 1
                    left += 1
                res = max(res, right - left + 1)
        return res