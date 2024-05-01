from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import (
    async_to_sync
)
from .models import Notification


@receiver(post_save, sender=Notification)
def send_message_notification(sender, instance, **kwargs):
    notify_count = Notification.objects.all().filter(checked=False).count()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_group", {
            "type": "notify.send",
            "count": notify_count
        }
    )
