class Solution:
    def findLucky(self, arr: list[int]) -> int:
        
        freq = {}

        for i in arr:
            freq[i] = freq.get(i,0) + 1

        min_freq = max_freq = -1
        for i in freq:
            if freq[i] == i:
                min_freq = i
                max_freq = max(min_freq, max_freq)
        return max_freq
        