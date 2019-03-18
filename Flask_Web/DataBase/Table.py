from Database import db, Role, User

db.create_all()
admin_role = Role(name = 'Admin')
mod_role = Role(name = 'Moderator')
user_role = Role(name = 'User')
user_john = User(username = 'john', role = admin_role)
user_susan = User(username = 'susan', role = user_role)
user_david = User(username = 'david', role = user_role)  # 到此这些对象只存在于Python中，还未写入数据库,id的值为None

# 对数据库的改动通过数据库会话管理，准备将对象写入数据库之前，要先添加到会话中
# 可直接写成：db.session.add_all([admin_role,mod_role,user_role,user_john,user_susan,user_david])
db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)

# 把对象写入数据库，调用commit()方法提交会话
db.session.commit()
