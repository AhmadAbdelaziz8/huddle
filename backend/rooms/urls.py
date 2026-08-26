from django.urls import path
from .views import RoomCreateView

urlpatterns = [
    path("", RoomCreateView.as_view(), name="room-create")
]
