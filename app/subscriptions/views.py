from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
# 구독 관련 REST API

# SubscriptionList
# api/v1/subscription
# [GET]: pk = 나 자신. (pk 입력받을 필요X)
# [POST]: 구독 하기
class SubscriptionList(APIView):
    # ToDo: 유저가 구독하고 있는 유튜버의 리스트는 따로 해야 하나요? (현민)
    # - 내가 구독하고 있는 유튜버들 리스트 (내가 구독한)
    def get(self, request):
        subs = Subscription.objects.filter(subscriber=request.user)
        # objects -> json
        serializer = SubSerializer(subs, many=True)
        return Response(serializer.data)

    # 좋아요/싫어요 기능 구현
    # 채팅 - 실시간 소켓 / 방 구분 / HTML
    # 냥이집사님

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
from .models import Subscription
class SubscriptionDetail(APIView):
    def get(self, request, pk):
        # 나를 구독한 사람들
        # api/v1/sub/{pk} -> 1번 유저가 구독한 사람들의 리스트가 궁금한 거죠.
        subs = Subscription.objects.filter(subscribed_to=pk) # objects -> json
        serializer = SubSerializer(subs, many=True)

        return Response(serializer.data) # 200

    # api/v1/sub/{pk}
    def delete(self, request, pk):
        sub = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        sub.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)