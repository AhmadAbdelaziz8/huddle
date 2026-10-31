from django.urls import path

from .views import RoomDetailView, RoomListCreateView

urlpatterns = [
    path("", RoomListCreateView.as_view(), name="room-create"),
    path("<uuid:pk>/", RoomDetailView.as_view(), name="room-detail"),
]
