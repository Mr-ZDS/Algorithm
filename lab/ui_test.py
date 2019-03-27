class lab1:
    list=[]
    Keyword = ['void', 'int', 'char', 'float', 'double', 'bool', 'long', 'short', 'signed', 'unsigned', 'true', 'false',
               'const', 'inline', 'auto', 'static', 'extern', 'register', 'for', 'while', 'if', 'else', 'do', 'switch',
               'case', 'default', 'break', 'continue', 'return', 'goto', 'new', 'delete', 'sizeof', 'class', 'struct',
               'enum', 'union', 'typedef', 'this', 'friend', 'virtual', 'mutable', 'explicit', 'operator', 'private',
               'protected', 'public', 'template', 'namespace', 'using', 'catch', 'throw', 'try', 'and', 'or', 'and_eq',
               'bitand', 'compl', 'not', 'not_eq', 'or_eq', 'xor', 'xor_eq', 'asm', 'export', 'typeid', 'volatile',
               'cout', 'main']
    Symbol1 = ['>', '<', '{', '}', '(', ')', '[', ']',  ';', ':', '+', '-', '*', '/',
          '.', '~', '!', '&', '%', '^', '|', '=', ',', '#']
    Symbol2 = ['>>', '<<', '+=', '-=', '*=', '/=', '%=', '&&', '::', '++', '--', '==', '!=', '>=', '<=', '->', '||']

    def __init__(self, str):
        self.str = str

    def Iskey(self, str):
        for i in self.Keyword:
            if str == i:
                return True

    def Is1(self, str):
        for i in self.Symbol1:
            if str == i:
                return True

    def Is2(self, str):
        for i in self.Symbol2:
            if str == i:
                return True

    def Is(self):
        str = self.str+' '
        length = len(str)
        str_visit = ''
        first = ''
        visit=''
        i = 0
        while i < length:
            ch = str[i]
            i += 1

            if str_visit == '':  # 如果存储字符串为空，将首个字符加进存储字符串中
                str_visit += ch
                first = ch
                if str_visit == ' ':
                    str_visit = ''
                continue

            if first.isdigit():  # 判断以数字开头的字符串
                if ch.isdigit():
                    str_visit += ch
                    continue
                elif i == length:
                    print(str_visit, '    数字')
                    self.list.append(str_visit+ '    数字')
                    break

                else:
                    print(str_visit, '    数字')
                    self.list.append(str_visit+ '    数字')
                    str_visit = ''
                    first = ''
                    i -= 1
                    continue;


            elif self.Is1(first):  # 以特殊符号开头
                if self.Is1(ch):
                    visit=str_visit+ch
                    if self.Is2(visit):
                        print(visit, '    特殊符号')
                        self.list.append(visit+ '    特殊符号')
                        str_visit = ''
                        visit=''
                        first = ''
                    else:
                        print(str_visit,'   特殊符号')
                        self.list.append(str_visit+ '    特殊符号')
                        i-=1
                        str_visit=''
                        first=''
                        continue

                else:
                    print(str_visit, '    特殊符号')
                    self.list.append(str_visit+'     特殊符号')
                    i -= 1  # 回退一位
                    str_visit = ''
                    first=''
                    continue

            elif first.isalpha():  # 判断以字母开头的字符串
                if ch.isalpha():
                    str_visit += ch
                    continue
                elif ch.isdigit():
                    str_visit += ch
                    continue
                elif ch == '_':
                    str_visit += ch
                    continue

                else:
                    if self.Iskey(str_visit):
                        print(str_visit,'    关键字')
                        self.list.append(str_visit+'     关键字')
                    else:
                        print(str_visit,'      标识符')
                        self.list.append(str_visit+'     标识符')
                    str_visit = ''
                    first = ''
                    i -= 1

            else:
                print('Error!!!!')



import tkinter
from tkinter import *
import tkinter.filedialog
from Analysis import lab1
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
            t1=lab1(line)
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
