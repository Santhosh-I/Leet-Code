class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:

        freq = {}
        nums = list(set(nums1)) + list(set(nums2))

        for i in nums:
            freq[i] = freq.get(i,0) + 1

        for i in nums1:
            if freq[i] > 1:
                return i
        else:
            return -1
        