class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        freq = {}
        majority = []

        for i in nums:
            freq[i] = freq.get(i,0) + 1

        for i in freq:
            majority.append(freq[i])

        for i in freq:
            if freq[i] == max(majority):
                return i
            
        