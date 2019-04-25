class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        visit = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[visit] = nums[i]
                visit += 1
        return visit
