import csv
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from apps.core.models import Course, Enrollment, Grade
from apps.core.services.grade_service import ScheduleConflictDetectorService, TriviaQuizImporterService

class TeacherRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_teacher()

class AuditLogMixin:
    def dispatch(self, request, *args, **kwargs):
        print(f"[AUDIT LOG] User '{request.user.username}' accessed backend path: {request.path}")
        return super().dispatch(request, *args, **kwargs)

class CourseListView(LoginRequiredMixin, AuditLogMixin, ListView):
    model = Course
    template_name = 'core/course_list.html'
    context_object_name = 'courses'
    paginate_by = 10

    def get_queryset(self):
        """Overrides generic queryset to inject live search filters."""
        queryset = Course.objects.all().select_related('teacher')
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query) | queryset.filter(code__icontains=search_query)
        return queryset

class EnrollInCourseView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, id=self.kwargs['course_id'])
        
        if ScheduleConflictDetectorService.has_conflict(request.user, course):
            messages.error(request, f"Enrollment Failed! This course conflicts with your current schedule.")
            return redirect('core:course_list')
        
        Enrollment.objects.get_or_create(student=request.user, course=course)
        messages.success(request, f"Successfully enrolled in {course.name}!")
        return redirect('core:course_list')


class ImportCourseQuizView(TeacherRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        course_id = self.kwargs['course_id']
        quizzes_imported = TriviaQuizImporterService.import_quiz_bank(course_id)
        
        if quizzes_imported > 0:
            messages.success(request, f"Successfully imported {quizzes_imported} quiz records from Trivia API!")
        else:
            messages.error(request, "Failed to import quizzes or no new quizzes found.")
        return redirect('core:course_list')

class ExportTranscriptCSVView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        student_id = self.kwargs['student_id']
        
        if request.user.is_student() and request.user.id != int(student_id):
            return HttpResponse("Access Denied: You can only view your own records.", status=403)
            
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="transcript_student_{student_id}.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Course Code', 'Course Name', 'Assignment', 'Type', 'Score', 'Max Score'])
        
        grades = Grade.objects.filter(enrollment__student_id=student_id).select_related('enrollment__course')
        for grade in grades:
            writer.writerow([
                grade.enrollment.course.code,
                grade.enrollment.course.name,
                grade.assignment_name,
                grade.type,
                grade.score,
                grade.max_score
            ])
        return response
