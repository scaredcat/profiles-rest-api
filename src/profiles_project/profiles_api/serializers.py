from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
  """Serializesrs a name field for testing our APIView."""

  name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.modelSerializer):
  """A serializer for our user profile objects."""

  