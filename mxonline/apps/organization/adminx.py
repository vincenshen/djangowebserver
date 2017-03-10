# -*- coding:utf-8 -*-

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ("name", "add_time")
    list_filter = ("name", "add_time")
    search_fields = ("name", )


class CourseOrgAdmin(object):
    list_display = ("name", "desc", "click_nums", "fav_nums", "image", "address", "city")
    list_filter = ("name", "desc", "click_nums", "fav_nums", "image", "address", "city__name")
    search_fields = ("name", "disc", "click_nums", "fav_nums", "image", "address", "city__name")


class TeacherAdmin(object):
    list_display = ("org", "name", "work_years", "work_company", "work_position", "points", "click_nums", "fav_nums", "add_time")
    list_filter = ("org__name", "name", "work_years", "work_company", "work_position", "points", "click_nums", "fav_nums", "add_time")
    search_fields = ("org_name", "name", "work_years", "work_company", "work_position", "points", "click_nums", "fav_nums")


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
