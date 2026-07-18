from django.db import models
from django.conf import settings

# Create your models here.

class Activity(models.Model):
    """
    Model representing an activity that wastes time (e.g., "Doom Scrolling", "Watching TV")."""
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name
    

class ActivityLog(models.Model):
    """
    Model represent a log entry from a user for a specific activity. Each log entry is associated with an activity and contains the duration of time spent on that activity.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    duration_minutes = models.PositiveIntegerField()

    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity.name} - {self.duration_minutes} minutes - {self.logged_at} "