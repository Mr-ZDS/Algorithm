class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        if nums[0] == 0 and nums[1] == 0 and nums[2] == 0:
            return [[0, 0, 0]]

        test = []
        for i in range(len(nums) - 2):
            j = i + 1
            last = len(nums) - 1
            while j < last:
                visit = nums[i] + nums[j] + nums[last]
                if visit == 0:
                    test += [nums[i], nums[j], nums[last]]
                if visit > 0:
                    last -= 1
                else:
                    j += 1
        if len(test) == 0:
            return []

        length = int(len(test) / 3)
        li = [[0 for i in range(3)] for j in range(length)]

        for i in range(0, len(test), +3):
            k = int((i + 1) // 3)
            for j in range(k, length):
                li[j][0], li[j][1], li[j][2] = test[i], test[i + 1], test[i + 2]
                break
        list2 = list(set([tuple(t) for t in li]))  # 二维list去重
        return list2
