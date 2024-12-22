from django.contrib import admin
from django.db import models
from course.models import Course, Students, Tutor
from course.models import Subject


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    list_filter = ['course']


admin.site.register(Course, CourseAdmin)
admin.site.register(Subject)
admin.site.register(Students)
admin.site.register(Tutor)


