from django.db import models
from common.models import CommonModel

# ChatRoom 모델을 분리했을 때의 이점
# - 관리의 용이
# - 확장성 (채팅방: 오픈채팅방, 업무채팅방-비밀번호 입력해야 들어갈 수 있다)
class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)

class ChatMessage(CommonModel):
    # 정보통신법 3개월 채팅 보관
    # SET_NULL - sender null 값으로 두겠다는 뜻. 1번 -> 계정삭제 -> null
    sender = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True) # 알수없음
    message = models.TextField()
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

# User:Msg(FK) => 1:N
    # - User: Msg, Msg, Msg => O
    # - Msg: User, User, User => X

# Room(부모) - 메세지(자녀)
# Room:Msg(FK) => 1:N
    # - Room: Msg, Msg, Msg => O
    # - Msg: Room, Room, Room => X