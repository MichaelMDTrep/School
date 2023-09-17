from django.contrib import admin
from .models import CourseCategory, Course, CourseCompleted, CourseLink

# Register your models here.

class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

    fields = (
        'name',
        'friendly_name'
    )

    ordering = ('name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
    )

    fields = (
        'title',
        'content',
        'category',
    )

    ordering = ('title',)


class CourseCompletedAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date',
        'course',
    )

    fields = (
        'user',
        'date',
        'course',
    )

    ordering = ('date',)


class CourseLinkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'course',
    )

    fields = (
        'name',
        'course',
        'link',
    )

    ordering = ('name',)


admin.site.register(CourseCategory, CourseCategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseCompleted, CourseCompletedAdmin)
admin.site.register(CourseLink, CourseLinkAdmin)