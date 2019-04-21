class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return
        for i in range(len(nums)):
            visit = target - nums[i]
            if visit in nums and nums.index(visit) != i:
                return [i, nums.index(visit)]
        return
