from .models import ChatRoom, ChatMessage
from rest_framework.serializers import ModelSerializer

class ChatRoomSerializer(ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = "__all__"

class ChatMessageSerializer(ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"
        read_only_fields = ["room", "sender"]
        depth = 1