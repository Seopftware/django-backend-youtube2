from django.shortcuts import render
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerializer

from rest_framework.response import Response
from rest_framework import status

# Video와 관련된 REST API
# 1.VideoList
# api/v1/video
# [GET]: 전체 비디오 목록 조회
# [POST]: 새로운 비디오 생성
# [PUT], [DELETE]: X
class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.all() # QuerySet[Video, Video, Video, Video, Video ....]
        # 직렬화 (Object -> Json) - Serializer(내가 원하는 데이터만 내려주는 기능)

        serializer = VideoSerializer(videos, many=True) # 쿼리셋 안 데이터가 2개 이상일 때

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data # Json -> Object(역직렬화)
        serializer = VideoSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2.VideoDetail
# api/v1/video/{video_id}
# [GET]: 특정 비디오 조회
# [POST]: X
# [PUT]: 특정 비디오 업데이트
# [DELETE]: 특정 비디오 삭제
    
# class VideoDetail():
#     def get():
#         pass

#     def put():
#         pass

#     def delete():
#         pass