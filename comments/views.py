from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from django.shortcuts import redirect

# Django Rest Framework for seeing the JSON
@api_view(['POST'])
def add_comment(request):
    # Make a serializer with the json from the request
    serializer = CommentSerializer(data=request.data)
    # Checks that the json has the right fields
    if serializer.is_valid():
        # Saves the object to the database
        serializer.save()
        return redirect("/")

# Display the comments
def blog_post(request):


    # get all the comments
    comments =Comment.objects.all()

    # render
    return render(request,
                    template_name="index.html",
                    context={'comments': comments})

# def add_comment():
#         serializer = CommentSerializer(data=request.POST)
#         # Checks that the json has the right fields
#         if serializer.is_valid():
#             # Saves the object to the database
#             serializer.save()
# 
        # return redirect("/")