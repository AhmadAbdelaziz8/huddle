from django.urls import path

from . import views

urlpatterns = [
    path("", views.RoomListCreateView.as_view(), name="room-list-create"),
    path("<uuid:pk>/", views.RoomDetailView.as_view(), name="room-detail"),
]
