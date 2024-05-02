from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import (
    Notification
)


def get_home(request):
    return render(request, template_name="home.html")


def get_dashborad(request):
    return render(request, template_name="dashboard.html")


def get_notification(request):
    return render(request, template_name="all_notification.html")


@login_required
def clear_notifications(request):
    Notification.objects.filter(
        user_ref=request.user, checked=False).update(checked=True)
    return JsonResponse({'success': True})


# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import (
#     Notification
# )


# def get_home(request):
#     return render(request, template_name="home.html")


# def get_dashborad(request):
#     return render(request, template_name="dashboard.html")


# def get_notification(request):
#     return render(request, template_name="all_notification.html")


# def clear_notifications(request):
#     Notification.objects.filter(checked=False).update(checked=True)
#     return JsonResponse({'success': True})
