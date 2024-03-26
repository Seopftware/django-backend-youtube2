from channels.generic.websocket import AsyncWebsocketConsumer
import json

# 코파일럿: GPT (개발자 대체가 아니라 개발자 생산성 향상)
    # - 굿뉴스: IT시장이 커진다. (건설회사) 
    # => 작업자 조끼,헬맷에 IOT
    # => 드론이 현장 촬영 / 사고 미연에 방지
    # LLM -> 100명 => 개발자 10명
    # 개발자의 최대 큰 장점:
    # - 이직 (갈 수 있는 곳이 정말 많아) // 컴포트 존 벗어나기
    # - 베스트 케이스 (Q&A)

# Consumer Class: Websocket연결을 처리하는 부분
# channel layer - group단위로 (Socket연결)
class ChatConsumer(AsyncWebsocketConsumer):
    # 소켓 연결
    async def connect(self):
            self.room_id = self.scope['url_route']['kwargs']['room_id']
            self.room_group_name = 'chat_' + str(self.room_id)

            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
    
    # 양방향 - 데이터 실시간 소통 통로
    async def receive(self, text_data):
        data_json = json.loads(text_data) # {'payload':data, 'status':}
        message = data_json.get('message')

        await self.channel_layer.group_send(self.room_group_name, {
             'type': 'chat_message',
             'message': message
        })

    async def chat_message(self, event):
         msg = event['message']
        #  email = event['email']

         await self.send(text_data=json.dumps({
              'type':'chat.message',
              'message': msg,
            #   'email': email
         }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)