class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        res = []

        for c in s:
            if c.isalnum() == True:
                res.append(c)

        if res == res[::-1]:
            return True
        else:
            return False
        