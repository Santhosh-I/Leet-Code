class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        avg = sum(nums[:k])
        max_avg = avg

        for i in range(k,len(nums)):

            avg += nums[i] - nums[i-k]
            
            max_avg = max(max_avg, avg)
        
        return max_avg / k
            
