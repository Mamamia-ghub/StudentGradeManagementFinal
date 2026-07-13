from django.contrib import admin
from apps.core.models import Course, Enrollment, Grade, Attendance

class GradeInline(admin.TabularInline):
    model = Grade
    extra = 1 

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'teacher', 'semester', 'year', 'start_time', 'end_time')
    search_fields = ('code', 'name', 'teacher__username')
    list_filter = ('semester', 'year')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    search_fields = ('student__username', 'course__code', 'course__name')
    list_filter = ('course__semester', 'course__year')
    inlines = [GradeInline] 

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'assignment_name', 'type', 'score', 'max_score', 'graded_at')
    search_fields = ('assignment_name', 'enrollment__student__username', 'enrollment__course__code')
    list_filter = ('type', 'graded_at')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'date', 'status')
    search_fields = ('enrollment__student__username',)
    list_filter = ('status', 'date')
