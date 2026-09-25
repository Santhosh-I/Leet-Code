class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        nums.sort()
        arr = []
        for i in nums:
            if i not in arr:
                arr.append(i)

        if len(arr) == 1:
            return arr[0]
        elif len(arr) == 2:
            return arr[1]
        else:
            return arr[-3]
        