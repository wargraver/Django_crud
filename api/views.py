from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from .serializers import SnippetSerializer
from rest_framework.parsers import JSONParser
from .models import user

# Create your views here.
@api_view(['GET',])
def get_view(request,slug):
    try:
        current_user  = user.objects.get(username = slug)
    except user.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    data = SnippetSerializer(current_user)
    return Response(data.data)
    

@api_view(['POST',])
def post_view(request):
    print(request)
    data = JSONParser().parse(request)
    print(data)
    try:
        current_user  = user.objects.get(username = data['username'])
    except user.DoesNotExist:
        serializer = SnippetSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
        return Response(data)
    data["error"] = "User Already Exists"
    return Response(data)
    


