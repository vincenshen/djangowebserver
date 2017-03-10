# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-

from django.conf.urls import url, include

from .views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateInfoView


urlpatterns = [

    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),
    # 修改头像
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),

    # 用户中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="upload_pwd"),

    # 发送邮箱验证码
    url(r'^sendmail_code/$', SendEmailCodeView.as_view(), name="sendmail_code"),

    url(r'^update/info/$', UpdateInfoView.as_view(), name="update_info"),
]