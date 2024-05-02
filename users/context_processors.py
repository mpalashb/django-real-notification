from .models import Notification


def notifications_processor(request):
    notifications = Notification.objects.all()
    try:
        notifications_with_user = notifications.filter(
            user_ref=request.user, checked=False)
    except:
        notifications_with_user = []
    try:

        unchecked_notifications_count = notifications.filter(
            user_ref=request.user, checked=False).count()
    except:
        unchecked_notifications_count = 0

    return {'notifications': notifications_with_user, 'unchecked_notifications_count': unchecked_notifications_count}


# from .models import Notification


# def notifications_processor(request):
#     notifications = Notification.objects.all()
#     unchecked_notifications_count = notifications.filter(checked=False).count()
#     return {'notifications': notifications, 'unchecked_notifications_count': unchecked_notifications_count}
