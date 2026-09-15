class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        freq = {}
        occurrence = []

        for i in arr:
            freq[i] = freq.get(i,0) + 1
        for i in set(arr):
            occurrence.append(freq[i])

        return len(occurrence) == len(set(occurrence))
            


        

        