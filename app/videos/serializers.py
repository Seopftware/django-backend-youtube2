from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer

class VideoListSerializer(serializers.ModelSerializer):
    # Video:User => Video(FK) -> User
    user = UserSerializer(read_only=True) # Video(FK)

    class Meta:
        model = Video
        fields = "__all__"


class VideoDetailSerializer(serializers.ModelSerializer):

    # Video:User => Video(FK) -> User
    user = UserSerializer(read_only=True) # Video(FK)

    # Video:Comment => Video -> Comment(FK) 
    # - Reverse Accessor
    # - 부모가 자녀를 찾을 때 => _set으로 부모에 속한 자녀들을 모두 찾을 수 있다.
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = "__all__"
        # depth = 1