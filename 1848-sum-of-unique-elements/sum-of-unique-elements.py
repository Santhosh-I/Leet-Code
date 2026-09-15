class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        freq = {}
        unique = []

        for i in nums:
            freq[i] = freq.get(i,0) + 1

        for i in nums:
            if freq[i] == 1:
                unique.append(i)

        return sum(unique)
