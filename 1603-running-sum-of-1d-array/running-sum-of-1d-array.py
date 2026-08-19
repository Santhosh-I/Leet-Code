class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        empty = [nums[0]]

        for i in range(1,len(nums)):
            empty.append(nums[i]+empty[i-1])


        return empty
        