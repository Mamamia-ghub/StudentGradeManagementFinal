import requests
from django.db import transaction
from apps.core.models import Enrollment, Course, Grade
import html

class GPACalculatorService:
    """Service 1: Computes weighted performance data across academic enrollments."""
    
    @staticmethod
    def calculate_gpa(student_user) -> float:
        enrollments = Enrollment.objects.filter(student=student_user)
        if not enrollments.exists():
            return 0.0

        total_points = 0.0
        total_credits = 0

        for enrollment in enrollments:
            grades = enrollment.grades.all()
            if not grades.exists():
                continue
            
            pct_sum = sum((g.score / g.max_score) for g in grades)
            avg_pct = (pct_sum / grades.count()) * 100

            if avg_pct >= 90: gpa_point = 4.0
            elif avg_pct >= 80: gpa_point = 3.0
            elif avg_pct >= 70: gpa_point = 2.0
            elif avg_pct >= 60: gpa_point = 1.0
            else: gpa_point = 0.0

            course_credits = enrollment.course.credits
            total_points += (gpa_point * course_credits)
            total_credits += course_credits

        return round(total_points / total_credits, 2) if total_credits > 0 else 0.0

class TriviaQuizImporterService:
    """Service 2: Safely handles external API connectivity and idempotency states."""
    
    @staticmethod
    def import_quiz_bank(course_id: int) -> int:
        url = "https://opentdb.com/api.php?amount=10&type=multiple"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                return 0
            
            data = response.json()
            results = data.get('results', [])
            
            created_count = 0
            enrollments = Enrollment.objects.filter(course_id=course_id)
            
            with transaction.atomic():
                for item in results:
                    raw_question = html.unescape(item['question'])
                    assignment_name = f"Quiz: {raw_question[:60]}"
                    
                    for enrollment in enrollments:
                        if not Grade.objects.filter(enrollment=enrollment, assignment_name=assignment_name).exists():
                            Grade.objects.create(
                                enrollment=enrollment,
                                assignment_name=assignment_name,
                                type='QUIZ',
                                score=0.0, 
                                max_score=10.0 
                            )
                            created_count += 1
            return created_count
        except requests.RequestException:
            return 0



class ScheduleConflictDetectorService:
    """
    Signature Algorithm: Interval-overlap verification logic.
    Variant (seed%2 = 0): Strict matching interval tracking.
    """
    
    @staticmethod
    def has_conflict(student_user, target_course: Course) -> bool:
        existing_enrollments = Enrollment.objects.filter(student=student_user).select_related('course')
        
        target_start = target_course.start_time
        target_end = target_course.end_time
        target_days = set(target_course.days_of_week.split(','))

        for enrollment in existing_enrollments:
            current_course = enrollment.course
            current_days = set(current_course.days_of_week.split(','))
            
            if target_days.intersection(current_days):
                curr_start = current_course.start_time
                curr_end = current_course.end_time
                
                if (target_start < curr_end) and (target_end > curr_start):
                    return True
        return False
