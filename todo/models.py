from django.db import models

class Task(models.Model):
    """Task model adding reterving tasks"""

    title = models.CharField(max_length=50)
    timestamp = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed', 'timestamp']