
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from rooms.serializers import RoomSerializer
from .models import Room

from django.shortcuts import get_object_or_404

class RoomCreateView(APIView):
    # list all rooms 
    def get(self,request):
        rooms = Room.objects.filter(is_active=True).order_by("-created_at")
        serializer=RoomSerializer(rooms, many=True, context={"request": request})
        return Response(serializer.data)
    
    # create room method 
    def post(self, request):
        # calls Django ORM, creates new room in the DB, returns instantiated python object of it 
        room = Room.objects.create()

        # Conver the python room model into native python data types 
        serializer = RoomSerializer(room, context={"request": request})

        # return the data, with the http code
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RoomDetailView(APIView):
    def get(self, request, pk):
        # get room id from the request
        room = get_object_or_404(Room, pk=pk, is_active=True)

        serializer = RoomSerializer(room, context={"request":request})

        return Response(serializer.data)

