from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import (
    async_to_sync
)
from .models import Notification


@receiver(post_save, sender=Notification)
def send_message_notification(sender, instance, **kwargs):
    notify_obj = Notification.objects.filter(
        user_ref=instance.user_ref, checked=False)
    user_ref = instance.user_ref
    notify_count = notify_obj.count()
    group_name = f"user_group_{user_ref.pk}"

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name, {
            "type": "notify.send",
            "ref_data": {
                "user_ref": {"username": user_ref.username, "userID": user_ref.pk},
                "count": notify_count
            }
        }
    )


# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from channels.layers import get_channel_layer
# from asgiref.sync import (
#     async_to_sync
# )
# from .models import Notification


# @receiver(post_save, sender=Notification)
# def send_message_notification(sender, instance, **kwargs):
#     notify_count = Notification.objects.all().filter(checked=False).count()
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         "notification_group", {
#             "type": "notify.send",
#             "count": notify_count
#         }
#     )
