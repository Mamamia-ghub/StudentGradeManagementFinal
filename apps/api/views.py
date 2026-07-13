from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.core.models import Course, Grade, Attendance
from apps.accounts.models import User
from apps.api.serializers import CourseSerializer, GradeSerializer, AttendanceSerializer, GPASerializer
from apps.api.permissions import IsTeacherOrStudentOwner

class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all().select_related('teacher')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class CourseGradesListAPIView(generics.ListAPIView):
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrStudentOwner]

    def get_queryset(self):
        """Filters grades down to the specific requested course id."""
        return Grade.objects.filter(enrollment__course_id=self.kwargs['id']).select_related('enrollment__student')

class GradeCreateAPIView(generics.CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrStudentOwner]

class StudentGPADetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.filter(role='STUDENT')
    serializer_class = GPASerializer
    permission_classes = [IsAuthenticated, IsTeacherOrStudentOwner]
    lookup_field = 'id'

class AttendanceListAPIView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrStudentOwner]

    def get_queryset(self):
        """Filters attendance list based on the enrollment URL parameter."""
        return Attendance.objects.filter(enrollment_id=self.kwargs['enrollment_id'])
