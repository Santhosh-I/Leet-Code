class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        comman = set(nums1).intersection(set(nums2))

        a,b = 0,0
        for i in comman:

            a += nums1.count(i)
            b += nums2.count(i)

        return [a,b]