#在全排列的基础上加判断条件变为N皇后求解
def permutation(Array, left, right):
    if left == right:
        for i in range(1,len(Array)-1):
            if Array[i]+1==Array[i+1] or Array[i]+1==Array[i-1] or Array[i]-1==Array[i-1] or Array[i]-1==Array[i+1]:
                i-=1
                break
        if i==len(Array)-2:
            print(Array)
    else:
        for i in range(left, len(Array)):
            Array[left], Array[i] = Array[i], Array[left]
            permutation(Array, left + 1, right)
            Array[left], Array[i] = Array[i], Array[left]


A = [0, 1, 2, 3]
permutation(A, 0, len(A) - 1)
