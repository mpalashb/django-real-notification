from django.db import models


class Message(models.Model):
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Message ID: {self.pk} -> {self.msg}"


class Notification(models.Model):
    msg_ref = models.ForeignKey("Message", on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)
