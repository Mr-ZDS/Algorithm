class analysis:
    list1=[]     #记录单词内容
    list2=[]     #记录单词类别
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

    # 判断是否为关键字
    def Iskey(self, str):
        for i in self.Keyword:
            if str == i:
                return True

    # 判断是否单特殊符号
    def Is1(self, str):
        for i in self.Symbol1:
            if str == i:
                return True

    # 判断双特殊符号
    def Is2(self, str):
        for i in self.Symbol2:
            if str == i:
                return True

    def Is(self):
        str = self.str + ' '
        length = len(str)
        str_visit = ''
        first = ''
        visit = ''
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
                    self.list1.append(str_visit)
                    self.list2.append('数字')
                    break
                else:
                    self.list1.append(str_visit)
                    self.list2.append('数字')
                    str_visit = ''
                    first = ''
                    i -= 1
                    continue;

            elif self.Is1(first):  # 以特殊符号开头
                if self.Is1(ch):
                    visit = str_visit + ch
                    if self.Is2(visit):
                        self.list1.append(visit)
                        self.list2.append('特殊符号')
                        str_visit = ''
                        visit = ''
                        first = ''
                    elif visit == '//':  # 如果是单行注释，则直接结束循环
                        break
                    else:
                        self.list1.append(str_visit)
                        self.list2.append('特殊符号')
                        i -= 1
                        str_visit = ''
                        first = ''
                        continue

                else:
                    self.list1.append(str_visit)
                    self.list2.append('特殊符号')
                    i -= 1  # 回退一位
                    str_visit = ''
                    first = ''
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
                        self.list1.append(str_visit)
                        self.list2.append('关键字')
                    else:
                        self.list1.append(str_visit)
                        self.list2.append('标识符')
                    str_visit = ''
                    first = ''
                    i -= 1

            elif first == '"':
                if ch == '"':
                    str_visit += ch
                    self.list1.append(str_visit)
                    self.list2.append('串')
                    str_visit = ''
                    first = ''
                else:
                    str_visit += ch
                continue

            else:
                print('Error!!!')