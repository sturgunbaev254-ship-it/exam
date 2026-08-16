from django.contrib import admin
from .models import Teacher, Group, Student, StudentMark


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'direction',
    )

    list_filter = (
        'direction',
    )

    search_fields = (
        'name',
    )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'mentor',
        'created_at',
    )

    list_filter = (
        'mentor',
    )

    search_fields = (
        'name',
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'age',
        'group',
        'created_at',
    )

    list_filter = (
        'group',
    )

    search_fields = (
        'name',
    )


@admin.register(StudentMark)
class StudentMarkAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'student',
        'subject',
        'mark',
        'created_at',
    )

    list_filter = (
        'subject',
        'mark',
    )

    search_fields = (
        'student__name',
        'subject',
    )