class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri = "".join(filter(str.isalnum, s)).lower()
        rev = stri[::-1]
        return stri == rev