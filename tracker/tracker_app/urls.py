from django.urls import path
from . import views

# Create url patterns
urlpatterns = [
    # Url for home page
    path('', views.index, name='index'),
    # Url for signup page
    path('signup/', views.signup, name='signup'),
]