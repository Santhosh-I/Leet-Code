class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:

        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0) + 1

        for i in freq:
            if freq[i] == 1 and i%2 == 0:
                return i
        else:
            return -1

        