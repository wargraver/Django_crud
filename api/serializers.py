from rest_framework  import serializers

from .models import user

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['username']