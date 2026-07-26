from django.shortcuts import render, redirect
from .models import Activity, ActivityLog
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.


def index(request):
    """
    View function for the home page of the tracker app.
    """

    if request.method == 'POST':
        if request.user.is_authenticated:
            duration = request.POST.get('duration_minutes')

            if duration:
                doom_scrolling_activity, created = Activity.objects.get_or_create(name='Doom Scrolling')

                ActivityLog.objects.create(
                    user=request.user,
                    activity=doom_scrolling_activity,
                    duration_minutes=duration
                )

        return redirect('index')



    if request.user.is_authenticated:
        user_logs = ActivityLog.objects.filter(user=request.user, activity__name='Doom Scrolling').order_by('-logged_at')
        duration_minutes_total_calculation = user_logs.aggregate(calculation=Sum('duration_minutes', default=0))
        total_duration = duration_minutes_total_calculation['calculation']
    else:
        user_logs = []
        total_duration = 0

    all_activities = Activity.objects.all()


    context = {
        'logs': user_logs,
        'activities': all_activities,
        'total_duration': total_duration
    }

    return render(request, 'tracker_app/index.html', context)



def signup(request):
    """
    View function for the signup page.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


