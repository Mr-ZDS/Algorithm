import os
from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash      #计算密码散列值
from flask_login import UserMixin,AnonymousUserMixin
from . import login_manager,db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# 配置数据库
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 此键设置为False，一边在不需要跟踪对象变化时降低内存消耗
db = SQLAlchemy(app)


#权限常量
class Permission:
    FOLLOW=1
    COMMIT=2
    WRITE=4
    MODERATE=8
    ADMIN=16


# 定义Role模型和User模型
class Role(db.Model):
    __tablename__ = 'roles'  # 定义表名
    # Flask-SQLAlchemy要求每个模型都定义主键,db.Colu mn类构造函数的第一个参数是数据库列和模型属性的类型，其余参数指定参数指定属性的配置选项
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)  # 值唯一，会话只能提交一次
    default = db.Column(db.Boolean, default = False, index = True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref = 'role', lazy = 'dynamic')  # lazy='dynamic'禁止自动查询

    def __init__(self,**kwargs):
        super(Role,self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions=0

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    #在数据库在创建角色
    @staticmethod
    def insert_roles():
        roles = {
            'User': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
            'Moderator': [Permission.FOLLOW, Permission.COMMENT,Permission.WRITE,Permission.MODERATE],
            'Administrator': [Permission.FOLLOW, Permission.COMMENT,Permission.WRITE, Permission.MODERATE,Permission.ADMIN],
        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name = r).first()
            if role is None:
                role = Role(name = r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email=db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64), unique = True, index = True)
    password_hash = db.Column(db.String(128))  # 加入密码散列
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 定义外键
    confirmed=db.Column(db.Boolean,default = False)


    #定义默认的用户角色
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(name = 'Administrator').first()
            if self.role is None:
                self.role = Role.query.filter_by(default = True).first()


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash.password)

    #生成一个令牌，有效期默认为一个小时
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id}).decode('utf-8')

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        return self.can(Permission.ADMIN)

class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser

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