class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = {}

        for i in s:
            freq[i] = freq.get(i,0) + 1

        for i in s:
            if freq[i] == 1:
                return s.index(i)
                break
        else:
            return -1        

        