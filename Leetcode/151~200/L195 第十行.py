'''
给定一个文本文件 file.txt，请只打印这个文件中的第十行。

示例:

假设 file.txt 有如下内容：

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
你的脚本应当显示第十行：

Line 10
'''

file=open('195.txt')
line=file.readline()
i=1
while line:
    if i>9:
        print(line)
        break
    i+=1
    line=file.readline()