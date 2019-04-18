# 先排序后遍历
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return None
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            last = len(nums) - 1
            while j < last:
                visit = nums[i] + nums[j] + nums[last]
                if visit == target:
                    return visit
                if abs(visit - target) < abs(result - target):
                    result = visit
                if visit > target:
                    last -= 1
                else:
                    j += 1
        return result
