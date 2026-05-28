class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(char for char in s if char.isalnum()).lower()

        start = 0
        end = len(st) -1

        while (start < end):
            if (st[start] != st[end]): return False
            start +=1
            end -=1
        return True