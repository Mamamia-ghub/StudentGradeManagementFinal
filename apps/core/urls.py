from django.urls import path
from apps.core import views

urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/<int:course_id>/enroll/', views.EnrollInCourseView.as_view(), name='enroll'),
    path('courses/<int:course_id>/import-quizzes/', views.ImportCourseQuizView.as_view(), name='import_quizzes'),
    path('students/<int:student_id>/transcript/csv/', views.ExportTranscriptCSVView.as_view(), name='export_transcript'),
]
