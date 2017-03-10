# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.db.models import Q
from django.views.generic.base import View
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage

from .models import Course
from utils.mixin_utils import LoginRequiredMixin


class CourseListView(LoginRequiredMixin, View):
    """
    课程列表
    """
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        hot_courses = Course.objects.all().order_by("-click_num")[:3]

        # 课程排序
        sort = request.GET.get("sort", "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            if sort == "hot":
                all_courses = all_courses.order_by("-click_num")

        # 课程分页
        try:
            page = request.GET.get("page", 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 3, request=request)
        courses = p.page(page)

        return render(request, "course-list.html", {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_courses
        })


class CourseDetailView(View):
    """
    课程详情
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.click_num +=1
        course.save()
        return render(request, "course-detail.html", {
            "course": course
        })
