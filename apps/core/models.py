from django.db import models
from django.conf import settings
from apps.core.managers import GradeManager

class Course(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'TEACHER'},
        related_name='taught_courses'
    )
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    credits = models.PositiveIntegerField(default=3)
    semester = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    
    start_time = models.TimeField()
    end_time = models.TimeField()
    days_of_week = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'STUDENT'},
        related_name='enrollments'
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_students')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.username} -> {self.course.code}"


class Grade(models.Model):
    TYPE_CHOICES = (
        ('EXAM', 'Exam'),
        ('QUIZ', 'Quiz'),
        ('HOMEWORK', 'Homework'),
        ('PROJECT', 'Project'),
    )
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='grades')
    assignment_name = models.CharField(max_length=200)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    score = models.FloatField()
    max_score = models.FloatField(default=100.0)
    graded_at = models.DateTimeField(auto_now_add=True)

    objects = GradeManager()

    def __str__(self):
        return f"{self.assignment_name}: {self.score}/{self.max_score}"


class Attendance(models.Model):
    STATUS_CHOICES = (
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('LATE', 'Late'),
    )
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.enrollment.student.username} - {self.date}: {self.status}"
