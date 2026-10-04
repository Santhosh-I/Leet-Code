class Solution:
    def isPalindrome(self, x: int) -> bool:

        y = str(x)
        z = [str(i) for i in y]

        start = 0
        end = len(y) - 1

        while start < end:
            z[start], z[end] = z[end], z[start]
            start += 1
            end -= 1

        return "".join(z) == str(x)