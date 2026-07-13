import pytest
from datetime import time
from django.contrib.auth import get_user_model
from apps.core.models import Course, Enrollment, Grade
from apps.core.services.grade_service import ScheduleConflictDetectorService, GPACalculatorService

User = get_user_model()

@pytest.mark.django_db
class TestAcademicCoreSuite:

    @pytest.fixture
    def setup_data(self):
        teacher = User.objects.create_user(username='proffox', password='pin', role='TEACHER')
        student = User.objects.create_user(username='alumni', password='pin', role='STUDENT')
        
        course_a = Course.objects.create(
            teacher=teacher, name='Advanced Backend Systems', code='CS301', credits=4,
            semester='Fall', year=2026, start_time=time(9, 0), end_time=time(10, 30), days_of_week='MWF'
        )
        course_b = Course.objects.create(
            teacher=teacher, name='Database Schema Design', code='CS302', credits=3,
            semester='Fall', year=2026, start_time=time(9, 30), end_time=time(11, 0), days_of_week='MWF'
        )
        course_c = Course.objects.create(
            teacher=teacher, name='Introduction to UI Design', code='CS101', credits=3,
            semester='Fall', year=2026, start_time=time(14, 0), end_time=time(15, 30), days_of_week='TTH'
        )
        return teacher, student, course_a, course_b, course_c

    def test_user_role_assignment(self, setup_data):
        _, student, _, _, _ = setup_data
        assert student.is_student() is True
        assert student.is_teacher() is False

    def test_course_creation_parameters(self, setup_data):
        _, _, course_a, _, _ = setup_data
        assert course_a.credits == 4
        assert course_a.code == 'CS301'

    def test_student_enrollment_registration(self, setup_data):
        _, student, course_a, _, _ = setup_data
        enrollment = Enrollment.objects.create(student=student, course=course_a)
        assert Enrollment.objects.filter(student=student, course=course_a).exists()
        assert enrollment.__str__() == "alumni -> CS301"

    def test_custom_manager_high_achievers_filter(self, setup_data):
        _, student, course_a, _, _ = setup_data
        enrollment = Enrollment.objects.create(student=student, course=course_a)
        
        Grade.objects.create(enrollment=enrollment, assignment_name='Quiz 1', type='QUIZ', score=95.0, max_score=100.0)
        Grade.objects.create(enrollment=enrollment, assignment_name='Quiz 2', type='QUIZ', score=50.0, max_score=100.0)
        
        high_achievers_count = Grade.objects.get_high_achievers().count()
        assert high_achievers_count == 1

    def test_signature_algorithm_detects_conflict(self, setup_data):
        _, student, course_a, course_b, _ = setup_data
        Enrollment.objects.create(student=student, course=course_a)
        
        conflict_detected = ScheduleConflictDetectorService.has_conflict(student, course_b)
        assert conflict_detected is True

    def test_signature_algorithm_allows_free_slot(self, setup_data):
        _, student, course_a, _, course_c = setup_data
        Enrollment.objects.create(student=student, course=course_a)
        
        conflict_detected = ScheduleConflictDetectorService.has_conflict(student, course_c)
        assert conflict_detected is False

    def test_gpa_service_calculation(self, setup_data):
        _, student, course_a, _, _ = setup_data
        enrollment = Enrollment.objects.create(student=student, course=course_a)
        Grade.objects.create(enrollment=enrollment, assignment_name='Final Exam', type='EXAM', score=92.0, max_score=100.0)
        
        computed_gpa = GPACalculatorService.calculate_gpa(student)
        assert computed_gpa == 4.0

    def test_gpa_service_failing_gpa(self, setup_data):
        _, student, course_a, _, _ = setup_data
        enrollment = Enrollment.objects.create(student=student, course=course_a)
        Grade.objects.create(enrollment=enrollment, assignment_name='Midterm', type='EXAM', score=35.0, max_score=100.0)
        
        computed_gpa = GPACalculatorService.calculate_gpa(student)
        assert computed_gpa == 0.0
