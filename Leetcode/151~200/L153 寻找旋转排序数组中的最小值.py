'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[len(nums) - 1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            else:
                if nums[l] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return nums[l]
