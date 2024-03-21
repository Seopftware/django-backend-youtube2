from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubSerializer
# Create your views here.
# 구독 관련 REST API

# SubscriptionList
# api/v1/subscription
# [POST]: 구독 하기
class SubscriptionList(APIView):
    def post(self, request):
        user_data = request.data # json -> object (Serializer)
        serializer = SubSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, 201)



# SubscriptionDeatail
# api/v1/subscription/{user_id}
# [GET]: 특정 유저의 구독자 리스트 조회
# [DELETE]: 구독 취소
class SubscriptionDetail(APIView):
    def get(self, request):
        pass

    def delete(self, request):
        pass