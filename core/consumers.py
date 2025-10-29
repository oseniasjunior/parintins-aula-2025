from channels.generic.websocket import AsyncJsonWebsocketConsumer


class SaleConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print('conectado')
        await self.accept()
        await self.channel_layer.group_add("sale", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("sale", self.channel_name)

    async def group_message(self, event):
        await self.send_json(content=event['content'])

    async def receive_json(self, event, **kwargs):
        await self.channel_layer.group_send(
            "sale",
            {
                "type": "group.message",  # deve corresponder ao nome do método
                "content": event['content'],  # aqui vai o conteúdo recebido
            },
        )
