def permutation(Array, left, right):
    if left == right:
        print(Array)
        '''
        #此段代码可在排列的基础上变为N皇后问题求解，即加一个判断条件
        for i in range(1,len(Array)-1):
            if Array[i]+1==Array[i+1] or Array[i]+1==Array[i-1] or Array[i]-1==Array[i-1] or Array[i]-1==Array[i+1]:
                i-=1
                break
        if i==len(Array)-2:
            print(Array)
        '''
    else:
        for i in range(left, len(Array)):
            Array[left], Array[i] = Array[i], Array[left]
            permutation(Array, left + 1, right)
            Array[left], Array[i] = Array[i], Array[left]


A = [0, 1, 2, 3]
permutation(A, 0, len(A) - 1)
