class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        start = 0
        end = len(needle)
        if haystack == needle:
            return 0

        while end < len(haystack):
            if haystack[start:end] == needle:
                return start
                break
            elif needle in haystack:
                return haystack.index(needle)
            start += 1
            end += 1
        else:
            return -1
        