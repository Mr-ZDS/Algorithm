# 先排序，注意时间复杂度

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def sort(list1, list2):
            i, j = 0, 0
            while j < len(list2):
                if i == len(list1):
                    list1.insert(i, list2[j])
                    i += 1
                    j += 1
                else:
                    if list1[i] <= list2[j]:
                        i += 1
                    else:
                        list1.insert(i, list2[j])
                        i += 1
                        j += 1
            return list1

        list1 = sort(nums1, nums2)
        length = len(list1)
        mid = length // 2
        if length % 2 == 0:
            return (list1[mid] + list1[mid - 1]) / 2
        else:
            return list1[mid]
