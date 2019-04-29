class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True
        visit = nums[0]
        for i in range(1, len(nums)):
            if visit < 1:
                return False
            visit -= 1
            visit = max(visit, nums[i])
        return True
