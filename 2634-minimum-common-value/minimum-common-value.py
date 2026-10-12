class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:

        dup = set(nums1).intersection(set(nums2))
        if dup:
            return min(dup)
        else:
            return -1
        