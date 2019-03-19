import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_mail import Mail, Message
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from threading import Thread

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


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 定义外键

    def __repr__(self):
        return '<User %r>' % self.username


mail = Mail(app)
# 配置Flask-Mail使用Gmail
app.config['MAIL_SERVER'] = 'xiansheng493@gmail.com'
app.config['MAIL_PORT'] = 90
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = ['Flasky']
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@foxmail.com>'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender = app.config['FLASKY_MAIL_SENDER'],
                  recipients = [to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators = [DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user = user)
        else:
            session['known'] = True
            session['name'] = form.name.data
            form.name.data = ''
            return redirect(url_for('index'))
            return render_template('index.html', form = form, name = session.get('name'),
                                   known = session.get('known', False))


# 设置异步发送电子邮件，把发送电子邮件的函数移到后台线程
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender = app.config['FLASKY_MAIL_SENDER'], recipients = [to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target = send_async_email, args = [app, msg])
    thr.start()
    return thr
