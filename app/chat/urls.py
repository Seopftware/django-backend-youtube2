from django.urls import path
from .views import ChatRoomList, ChatMessageList, chat_html

# api/v1/chat/room
# api/v1/chat/<room_id>/messages
urlpatterns = [
    path('room/', ChatRoomList.as_view(), name='room-list'), # room
    path('<int:room_id>/messages', ChatMessageList.as_view(), name='chat-message'), # message
    path('chatting', chat_html, name='chatting')
]