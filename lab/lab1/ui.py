import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from Analysis import analysis


class GUI():

    def __init__(self, name):
        self.name = name

    def creat(self):
        self.name.title('词法分析')
        self.name.geometry('450x370+350+120')  # 设置窗口大小和偏移度
        self.button1 = tkinter.Button(master = self.name, text = '选择文件', command = self.choose)
        self.button1.grid(row = 0, column = 11)
        self.button2 = tkinter.Button(self.name, text = '分析', command = self.tran)
        self.button2.grid(row = 6, column = 11)
        self.button3 = tkinter.Button(self.name, text = '写入', command = self.write)
        self.button3.grid(row = 5, column = 11)
        self.text = tkinter.Text(master = self.name, width = 55, height = 1)
        self.text.grid(row = 2, column = 7, columnspan = 6, rowspan = 1)
        self.text1 = tkinter.Text(master = self.name, width = 25)
        self.text1.grid(row = 3, column = 0, rowspan = 7, columnspan = 10)
        #表格定义
        self.tree = ttk.Treeview(master = self.name, columns = ('单词', '类别'), show = 'headings', height = 14)
        self.tree.column('单词', width = 90)  # 居中加入  anchor='center'
        self.tree.column('类别', width = 90)
        self.tree.heading('单词', text = '单词')
        self.tree.heading('类别', text = '类别')
        self.tree.grid(row = 3, column = 12, rowspan = 7, columnspan = 10)

    def choose(self):  # 打开并选择文件
        # 应该设置再次点击会清空文本框
        filenames = tkinter.filedialog.askopenfilenames()
        if len(filenames) != 0:
            filename = ""
            for i in range(0, len(filenames)):
                filename += str(filenames[i]) + "\n"
            self.Filename = filename  # 存取选择的文件路径
            self.text.insert(1.0, '文件路径为:' + filename)
        else:
            self.text.insert(1.0, "您没有选择任何文件");

    def write(self):
        self.text1.delete('1.0','end')        #每次写入时先清空文本框
        f = open(self.Filename.strip('\n'))  # 此时的路径结尾带有'\n'换行符，需要去掉
        line = f.readline()
        i = 1.0
        while line != '':
            self.text1.insert(i, line)
            i += 1.0
            line = f.readline()
        f.close()

    def tran(self):
        self.text1.delete('1.0','end')       #点击分析按钮时会清空文本框，之后输入压缩文本
        self.tree.delete(*self.tree.get_children())      #点击后清空表格内容
        f = open(self.Filename.strip('\n'))
        line = f.readline().strip('\n')
        i = 1  # 记录表格的行数
        result = ''
        while line != '':
            t1 = analysis(line)
            t1.Is()
            j = 0  # 记录list2列表的下标
            for lines in t1.list1:
                result += lines
                lines += '\n'
                self.tree.insert('', i, values = (lines, t1.list2[j]))
                i += 1
                j += 1
            j = 0
            t1.list1.clear()
            t1.list2.clear()
            line = f.readline().strip('\n')
        f.close()
        self.text1.insert(INSERT, result)


def start():
    gui = tkinter.Tk()
    windows = GUI(gui)
    windows.creat()
    gui.mainloop()


start()