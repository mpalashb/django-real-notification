from .models import Notification


def notifications_processor(request):
    notifications = Notification.objects.all()
    unchecked_notifications_count = notifications.filter(checked=False).count()
    return {'notifications': notifications, 'unchecked_notifications_count': unchecked_notifications_count}
