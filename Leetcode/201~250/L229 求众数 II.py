
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        v1, v2 = [], []
        result = []
        for i in nums:
            if i not in v1:
                v1.append(i)
                v2.append(1)
            else:
                v2[v1.index(i)] += 1

        for i in range(len(v2)):
            if v2[i] > (len(nums) / 3):
                result.append(v1[i])
        return result