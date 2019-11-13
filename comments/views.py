from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer


@api_view(['POST'])
def add_comment(request):
    # Make a serializer with the json from the request
    serializer = CommentSerializer(data=request.data)
    # Checks that the json has the right fields
    if serializer.is_valid():
        # Saves the object to the database
        serializer.save()
        # 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)