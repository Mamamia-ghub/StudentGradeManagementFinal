from rest_framework import serializers
from apps.core.models import Course, Grade, Attendance
from apps.accounts.models import User
from apps.core.services.grade_service import GPACalculatorService

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'teacher', 'name', 'code', 'credits', 'semester', 'year', 'start_time', 'end_time', 'days_of_week']

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'enrollment', 'assignment_name', 'type', 'score', 'max_score', 'graded_at']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'enrollment', 'date', 'status']

class GPASerializer(serializers.ModelSerializer):
    gpa = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'gpa']

    def get_gpa(self, obj):
        # Calls the Service Layer directly
        return GPACalculatorService.calculate_gpa(obj)