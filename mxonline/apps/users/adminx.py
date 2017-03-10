# -*- coding:utf-8 -*-
import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner, UserProfile
from xadmin.plugins.auth import UserAdmin


class UserProfileAdmin(UserAdmin):
    pass


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "教学在线后台管理系统"
    site_footer = "教学在线网"
    menu_style = "accordion"
    model_icon = 'fa fa-handshake-o'


class EmailVerifyRecordAdmin(object):
    list_display = ("code", "email", "send_type", "send_time")
    search_fields = ("code", "email", "send_type")
    list_filter = ("code", "email", "send_type", "send_time")
    model_icon = 'fa fa-handshake-o'


class BannerAdmin(object):
    list_display = ("title", "image", "url", "index", "add_time")
    search_fields = ("title", "image", "url", "index")
    list_filter = ("title", "image", "url", "index", "add_time")
    model_icon = 'fa fa-handshake-o'

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
# xadmin.site.register(UserProfile, UserProfileAdmin)
# from django.contrib.auth.models import User
# xadmin.site.unregister(User)

