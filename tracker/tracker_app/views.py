from django.shortcuts import render
from .models import Activity, ActivityLog
from django.db.models import Sum


# Create your views here.


def index(request):
    """
    View function for the home page of the tracker app.
    """

    user_logs = ActivityLog.objects.filter(user=request.user).order_by('-logged_at') if request.user.is_authenticated else []

    all_activities = Activity.objects.all()

    duration_minutes_total_calculation = user_logs.aggregate(calculation=Sum('duration_minutes'), default=0)

    total_duration = duration_minutes_total_calculation['calculation']

    context = {
        'logs': user_logs,
        'activities': all_activities,
        'total_duration': total_duration
    }

    return render(request, 'tracker_app/index.html', context)