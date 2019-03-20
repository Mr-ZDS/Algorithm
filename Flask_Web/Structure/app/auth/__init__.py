#创建身份验证蓝本
from flask import Blueprint

auth=Blueprint('auth',__name__)

from .import views
