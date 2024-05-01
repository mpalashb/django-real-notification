from channels.generic.websocket import (
    AsyncWebsocketConsumer
)
import json


class NotifyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "notification_group"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def notify_send(self, event):
        get_count = event['count']

        await self.send(text_data=json.dumps({
            "unread_count": get_count
        }))
