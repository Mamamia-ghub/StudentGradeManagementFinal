from django import template

register = template.Library()

@register.filter(name='percentage')
def percentage(score, max_score):
    """
    Calculates a clean percentage string for student grades.
    Usage in HTML: {{ grade.score|percentage:grade.max_score }} -> Outputs: "85.0%"
    """
    try:
        return f"{(float(score) / float(max_score)) * 100:.1f}%"
    except (ValueError, ZeroDivisionError, TypeError):
        return "0.0%"