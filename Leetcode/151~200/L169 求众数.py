class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, result = 0, nums[0]
        for i in nums[1:]:
            if i == result:
                count += 1
            elif count > 0:
                count -= 1
            else:
                result = i
        return result
