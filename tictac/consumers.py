import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GameRoom(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['code']
        self.room_group_name = f'room_{self.room_name}'
        print(self.room_group_name)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print(text_data)
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'run_game',
                'payload': text_data
            }
        )

    async def run_game(self, event):
        data = event['payload']
        data = json.loads(data)

        await self.send(text_data=json.dumps({
            'payload': data['data']
        }))
