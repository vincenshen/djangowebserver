# -*- coding:utf-8 -*-

from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from mxonline.settings import EMAIL_FROM


def random_str(randomlength=8):
    '''
    生成随机验证码
    :param randomlength: 验证码长度
    :return:
    '''
    ran_str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        ran_str +=chars[random.randint(0, length)]
    return ran_str


def send_register_email(email, send_type="register"):
    '''
    发送邮件功能
    :param email: 收件人地址
    :param send_type: 发送类型为 注册或找回密码
    :return:
    '''
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "图书管理系统注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        send_mail(email_title, email_body, EMAIL_FROM, [email])

    elif send_type == "forget":
        email_title = "图书管理系统密码重置链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/reset/{0}".format(code)

        send_mail(email_title, email_body, EMAIL_FROM, [email])

    elif send_type == "update_email":
        email_title = "图书管理系统邮箱修改验证码"
        email_body = "您的邮箱验证码为：{0}".format(code)

        send_mail(email_title, email_body, EMAIL_FROM, [email])