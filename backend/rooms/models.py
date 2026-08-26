import uuid

from django.db import models


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid7)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default= True)

