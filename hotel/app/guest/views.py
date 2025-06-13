from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GuestSerializer
from .models import Guest

# Create your views here.


@api_view(['POST'])
def create_guest(request):
    serializer = GuestSerializer(data=request.data)
    if serializer.is_valid():
        guest = serializer.save()
        return Response({"message": "Guest created", "guest": GuestSerializer(guest).data}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_guests(request):
    guests = Guest.objects.all()
    serializer = GuestSerializer(guests, many=True)
    return Response(serializer.data)