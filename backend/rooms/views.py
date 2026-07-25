from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Room
from .serializers import RoomSerializer


class RoomListCreateView(APIView):
    def post(self, request):
        room = Room.objects.create()
        join_url = request.build_absolute_uri(f"/api/rooms/{room.id}/")
        return Response(
            {"id": room.id, "join_url": join_url},
            status=status.HTTP_201_CREATED,
        )


class RoomDetailView(APIView):
    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        return Response(RoomSerializer(room).data)

    def delete(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
