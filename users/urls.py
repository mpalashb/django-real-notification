
from django.urls import path
from users.views import (
    get_dashborad, get_home,
    get_notification, clear_notifications,
)

app_name = 'users'

urlpatterns = [
    path('', get_home, name="homepage"),
    path('dashboard', get_dashborad, name="dashboard"),
    path('all-notification', get_notification, name="all-notify"),
    path('api/clear-notifications/', clear_notifications, name="clear-notify"),
]
