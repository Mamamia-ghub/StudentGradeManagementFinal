from django.db import models

class PerformanceQuerySet(models.QuerySet):
    def high_achievers(self):
        """Filters grades that scored 90% or higher on an assignment."""
        return self.filter(score__gte=models.F('max_score') * 0.9)

class GradeManager(models.Manager):
    def get_queryset(self):
        return PerformanceQuerySet(self.model, using=self._db)

    def get_high_achievers(self):
        """Exposes the custom QuerySet method straight through the manager."""
        return self.get_queryset().high_achievers()