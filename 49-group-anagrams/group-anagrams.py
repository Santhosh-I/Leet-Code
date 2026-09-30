class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        freq = {}

        for i in strs:
            s1 = "".join(sorted(i))

            if s1 in freq.keys():
                freq[s1].append(i)
            else:
                freq[s1] = [i]

        return list(freq.values())
