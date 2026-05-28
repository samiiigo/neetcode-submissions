class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri = "".join(char for char in s if char.isalnum()).lower()
        return stri == stri[::-1]