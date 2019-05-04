import pymysql


class Mysqltest:
    def __init__(self, host, user, password, database, port = 3306, charset = 'utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    # 获取连接的对象和执行对象
    def connect(self):
        self.conn = pymysql.connect(host = self.host, user = self.host,
                                    password = self.password, database = self.database,
                                    port = self.port, charset = self.charset)
        self.cur = self.conn.cursor()

    def fetchone(self, sql, params = None):
        dataOne = None
        try:
            count = self.cur.execute(sql, params)
            if count != 0:
                dataOne = self.cur.fetchone()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return dataOne

    def fetchall(self, sql, parms = None):
        dataall = None
        try:
            count = self.cur.execute(sql, parms)
            if count != 0:
                dataall = self.cur.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return dataall

    def __item(self, sql, parms = None):
        '''
        执行增删改
        :param sql:           sql语句
        :param params:        sql语句对象的参数列表，默认值为None
        :return:              受影响的行数
        '''
        count = 0
        try:
            count = self.cur.execute(sql, params)
            self.conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return count

    def update(self, sql, params = None):
        '''
        执行修改
        :param sql:     sql语句
        :param params:  sql语句对象的参数列表，默认值为None
        :return:        受影响的行数
        '''
        return self.__item(sql, params)

    def insert(self, sql, params = None):
        '''
        执行新增
        :param sql:     sql语句
        :param params:  sql语句对象的参数列表，默认值为None
        :return:        受影响的行数
        '''
        return self.__item(sql, params)

    def delete(self, sql, params = None):
        return self.__item(sql, params)

    def close(self):
        if self.cur != None:
            self.cur.close()
        if self.conn != None:
            self.conn.close()
