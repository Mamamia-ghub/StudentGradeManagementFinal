from django.urls import path
from apps.api import views

urlpatterns = [
    path('courses/', views.CourseListCreateAPIView.as_view(), name='api_courses'),
    path('courses/<int:id>/grades/', views.CourseGradesListAPIView.as_view(), name='api_course_grades'),
    path('grades/', views.GradeCreateAPIView.as_view(), name='api_grade_create'),
    path('students/<int:id>/gpa/', views.StudentGPADetailAPIView.as_view(), name='api_student_gpa'),
    path('attendance/<int:enrollment_id>/', views.AttendanceListAPIView.as_view(), name='api_attendance'),
]