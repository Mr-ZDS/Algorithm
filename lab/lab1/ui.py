import tkinter
from tkinter import *
import tkinter.filedialog
from Analysis import analysis
class GUI():

    def __init__(self,name):
        self.name=name

    def creat(self):
        self.name.title('词法分析')
        self.name.geometry('450x370+350+120')         #设置窗口大小和偏移度
        self.button1=tkinter.Button(master = self.name,text='选择文件',command=self.choose)
        self.button1.grid(row=0,column=11)
        self.button2=tkinter.Button(self.name,text='分析',command=self.tran)
        self.button2.grid(row=6,column=11)
        self.button3 = tkinter.Button(self.name, text = '写入', command = self.write)
        self.button3.grid(row = 5, column = 11)
        self.text=tkinter.Text(master = self.name,width=55,height=1)
        self.text.grid(row=2,column=7,columnspan=6,rowspan=1)
        self.text1=tkinter.Text(master = self.name,width=25)
        self.text1.grid(row=3,column=0,rowspan=7,columnspan=10)
        self.text2=tkinter.Text(master = self.name,width=25)
        self.text2.grid(row=3,column=12,rowspan=7,columnspan=10)

    def choose(self):        #打开并选择文件
        #应该设置再次点击会清空文本框
        filenames = tkinter.filedialog.askopenfilenames()
        if len(filenames) != 0:
            filename = ""
            for i in range(0, len(filenames)):
                filename += str(filenames[i]) + "\n"
            self.Filename=filename       #存取选择的文件路径
            self.text.insert(1.0, '文件路径为:'+filename)
        else:
            self.label.config(text = "您没有选择任何文件");

    def write(self):
        f=open(self.Filename.strip('\n'))         #此时的路径结尾带有'\n'换行符，需要去掉
        line=f.readline()
        i=1.0
        while line!='':
            self.text1.insert(i,line)
            i+=1.0
            line=f.readline()
        f.close()

    def tran(self):
        f=open(self.Filename.strip('\n'))
        line=f.readline().strip('\n')
        while line!='':
            t1=analysis(line)
            t1.Is()
            for lines in t1.list:
                lines+='\n'
                self.text2.insert(INSERT,lines)
            t1.list.clear()
            line = f.readline().strip('\n')
        f.close()




def start():
    gui=tkinter.Tk()
    windows=GUI(gui)
    windows.creat()
    gui.mainloop()

start()
