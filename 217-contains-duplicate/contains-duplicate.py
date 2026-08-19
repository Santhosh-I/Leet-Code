class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        without_duplicate = set(nums)

        if len(nums) != len(without_duplicate):
            return True
        else:
            return False
        