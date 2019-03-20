import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash      #计算密码散列值
from flask_login import UserMixin
from . import login_manager

# 配置数据库
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 此键设置为False，一边在不需要跟踪对象变化时降低内存消耗
db = SQLAlchemy(app)


# 定义Role模型和User模型
class Role(db.Model):
    __tablename__ = 'roles'  # 定义表名
    # Flask-SQLAlchemy要求每个模型都定义主键,db.Colu mn类构造函数的第一个参数是数据库列和模型属性的类型，其余参数指定参数指定属性的配置选项
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)  # 值唯一，会话只能提交一次
    users = db.relationship('User', backref = 'role', lazy = 'dynamic')  # lazy='dynamic'禁止自动查询

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email=db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64), unique = True, index = True)
    password_hash = db.Column(db.String(128))  # 加入密码散列
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 定义外键

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash.password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

'''
#密码散列功能测试
u1=User()
u1.password='cat'
#print(u.password)
print(u1.password_hash)
print(u1.verify_password('cat'))
print(u1.verify_password('dog'))
u2=User()
u2.password='cat'
print(u2.password_hash)
'''