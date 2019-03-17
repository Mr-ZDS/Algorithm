def quick_sort(array, l, r):
    if l < r:
        visit = partition(array, l, r)    #记录每趟排序后基准元素的位置
        quick_sort(array, l, visit - 1)
        quick_sort(array, visit + 1, r)

def partition(array, l, r):
    x = array[r]
    i = l-1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i+1

list = [1,4,8,33,63,7,5,2,8,5]
quick_sort(list, 0, len(list)-1)
print(list)

