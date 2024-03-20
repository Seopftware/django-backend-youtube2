from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer

class VideoSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True) # Video(FK)

    class Meta:
        model = Video
        fields = "__all__"
        # depth = 1