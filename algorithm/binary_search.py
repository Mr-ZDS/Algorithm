# 有序表的二分查找
import numpy


def Binary_search(list, value):
    low = 0
    high = len(list)
    while low < high:
        mid = int((low + high) / 2)
        if list[mid] > value:
            high = mid - 1
        elif list[mid] < value:
            low = mid + 1
        else:
            print(mid)
            return mid
    print('无法找到查找的值！！！')
    return False


# 随机数生成一个列表
list = numpy.random.randint(2, 20, size = 10)
list.sort()
print(list)
value = numpy.random.randint(20)
Binary_search(list, value)