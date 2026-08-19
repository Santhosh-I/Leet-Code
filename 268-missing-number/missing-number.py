class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        temp = (len(nums)+1) * [-1]  
        
        for num in nums:
            temp[num] = num
        for i in range(len(temp)):
            if temp[i] == -1:
                return i