class Solution:
    def isPalindrome(self, s: str) -> bool:

        txt = [c.lower() for c in s if c.isalnum()]

        return txt == txt[::-1]
        