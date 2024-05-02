from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from channels.generic.websocket import (
    AsyncWebsocketConsumer
)
import json


class NotifyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the user connected on client
        self.user = await self.get_user_with_scope()
        if self.user is None:
            await self.close()
        else:
            self.group_name = f"user_group_{self.user.id}"
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, "group_name"):
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def notify_send(self, event):
        retrive_data = event['ref_data']
        user_to = retrive_data['user_ref']
        get_count = retrive_data['count']

        await self.send(text_data=json.dumps({
            "user_to": user_to,
            "unread_count": get_count
        }))

    @database_sync_to_async
    def get_user_with_scope(self):
        user_id = self.scope["user"].id if self.scope["user"].is_authenticated else None
        if user_id:
            return User.objects.get(id=user_id)
        else:
            return None


# from channels.generic.websocket import (
#     AsyncWebsocketConsumer
# )
# import json


# class NotifyConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.group_name = "notification_group"
#         await self.channel_layer.group_add(
#             self.group_name,
#             self.channel_name
#         )

#         await self.accept()

#     async def disconnect(self, code):
#         await self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         )

#     async def notify_send(self, event):
#         get_count = event['count']

#         await self.send(text_data=json.dumps({
#             "unread_count": get_count
#         }))
