class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(len(nums)):
            if result > nums[i]:
                result = nums[i]
        return result
