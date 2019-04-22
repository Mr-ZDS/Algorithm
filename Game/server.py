from asyncore import dispatcher
from asynchat import async_chat
import asyncore, socket

PORT = 5005
NAME = 'TestChat'


class EndSession(Exception):
    pass


class CommandHandler:
    # 相应未知命令
    def unknown(self, session, cmd):
        session.push('Unknown command:{}s\r\n'.format(cmd))

    def handle(self, session, line):
        # 处理从指定会话收到的行
        if not line.strip():
            return
        # 提取命令
        parts = line.split(' ', 1)
        cmd = parts[0]
        try:
            line = parts[1].strip()
        except IndexError:
            line = ''
        # 尝试查找处理程序
        meth = getattr(self, 'do_' + cmd, None)
        try:
            meth(session, line)
        except TypeError:
            # 如果未知。响应未知命令
            self.unknown(session, cmd)


# 负责基本的命令处理和广播,通用环境
class Room(CommandHandler):
    def __init__(self, server):
        self.server = server
        self.sessions = []

    # 有用户进入聊天室
    def add(self, session):
        self.sessions.append(session)

    # 用户离开聊天室
    def remove(self, session):
        self.sessions.remove(session)

    # 广播一行内容
    def broadcast(self, line):
        for session in self.sessions:
            session.push(line)

    # 响应layout
    def do_layout(self, session, line):
        raise EndSession


# 为刚连接的用户准备的聊天室
class LoginRoom(Room):
    # 用户进入时系统发出问候
    def add(self, session):
        Room.add(self, session)
        self.broadcast('Welcome to {}\r\n'.format(self.server.name))

    # 除login和logout外的未知命令
    def unknown(self, session, cmd):
        session.push('Please log in\nUse "login <nick>"\r\n')

    def do_login(self, session, line):
        name = line.strip()
        # 确保输入了用户名
        if not name:
            session.push('Please enter a name\r\n')
        # 确保用户名未被占用
        elif name in self.server.users:
            session.push('The name "{}" is taken.\r\n'.format(name))
            session.push('Please try again.\r\n')
        else:
            # 存储到会话并移到主聊天室
            session.name = name
            session.enter(self.server.main_room)


# 多个用户准备的聊天室
class ChatRoom(Room):
    # 告诉别人有新用户进入
    def add(self, session):
        self.broadcast(session.name + 'has entered the room.\r\n')
        self.server.users[session.name] = session
        super().add(session)

    # 告诉用户有人离开
    def remove(self, session):
        Room.remove(self, session)
        self.broadcast(session.name + 'has left the room.\r\n')

    def do_say(self, session, line):
        self.broadcast(session.name + ':' + line + '\r\n')

    # 命令look用于查看聊天室还有哪个用户
    def do_look(self, session, line):
        session.push('The following are in this room:\r\n')
        for other in self.sessions:
            session.push(other.name + '\r\n')

    # 命令who用于查看谁已登录
    def do_who(self, session, line):
        session.push('The following are logged in:\r\n')
        for name in self.server.users:
            session.push(name + '\r\n')


# 用于将用户从服务器删除
class LogoutRoom(Room):
    # 将进入LogoutRoom的用户删除
    def add(self, session):
        try:
            del self.server.users[session.name]
        except KeyError:
            pass


# 负责处理服务器和单个用户通信
class ChatSession(async_chat):
    def __init__(self, server, sock):
        super().__init__(sock)
        self.server = server
        self.set_terminator("\r\n")
        self.data = []
        self.name = None
        self.enter(LoginRoom(server))

    # 从当前聊天室离开，并进入下一个聊天室
    def enter(self, room):
        try:
            cur = self.room
        except AttributeError:
            pass
        else:
            cur.remove(self)
        self.room = room
        room.add(self)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        try:
            self.room.handle(self, line)
        except EndSession:
            self.handle_close()

    def handle_close(self):
        async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))


# 只有一个聊天室的聊天服务器
class ChatServer(dispatcher):
    def __init__(self, port, name):
        super().__init__()
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()  # 能够重用原来的地址
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.users = {}
        self.main_room = ChatRoom(self)

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)


if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print()
