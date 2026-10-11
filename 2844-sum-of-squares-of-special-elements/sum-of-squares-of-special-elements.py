class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        n = len(nums)
        special = []

        for i in range(1,len(nums) + 1):
            if n % i == 0:
                special.append(nums[i - 1] ** 2)

        return sum(special)
        