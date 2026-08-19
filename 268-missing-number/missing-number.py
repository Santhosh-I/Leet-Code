class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sorted_list = sorted(nums)

        for i in range(len(nums)):
            if i == sorted_list[i]:
                continue
            else:
                return i
        else:
            return i + 1
        