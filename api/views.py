from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import SnippetSerializer

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
    
  

