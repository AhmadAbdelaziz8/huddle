from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from rooms.serializers import RoomSerializer
from .models import Room

class RoomCreateView(APIView):
    # create room method 
    def post(self, request):
        # calls Django ORM, creates new room in the DB, returns instantiated python object of it 
        room = Room.objects.create()

        # Conver the python room model into native python data types 
        serializer = RoomSerializer(room)

        # return the data, with the http code
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    