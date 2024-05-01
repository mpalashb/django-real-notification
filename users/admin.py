from django.contrib import admin
from .models import (
    Message, Notification,
)


@admin.register(Notification)
class NotificationModelAdmin(admin.ModelAdmin):
    list_display = ("msg_ref", ("checked"),)


admin.site.register(Message)
