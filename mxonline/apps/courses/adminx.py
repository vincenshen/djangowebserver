# -*- coding:utf-8 -*-
import xadmin
from .models import Course, CourseResource, Lesson, Video


class CourseAdmin(object):
    list_display = ("name", "desc", "detail", "degree", "learn_times", "students", "fav_nums", "image", "click_num", "add_time")
    search_fields = ("name", "desc", "detail", "degree", "learn_times", "students", "fav_nums", "image", "click_num")
    list_filter = ("name", "desc", "detail", "degree", "learn_times", "students", "fav_nums", "image", "click_num", "add_time")


class LessonAdmin(object):
    list_display = ("course", "name", "add_time")
    list_filter = ("course__name", "name", "add_time")
    search_fields = ("course__name", "name")


class VideoAdmin(object):
    list_display = ("lesson", "name", "add_time")
    list_filter = ("lesson__name", "name", "add_time")
    search_fields = ("lesson__name", "name")


class CourseResourceAdmin(object):
    list_display = ("course", "name", "download", "add_time")
    list_filter = ("course__name", "name", "download", "add_time")
    search_fields = ("course__name", "name", "download")


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
