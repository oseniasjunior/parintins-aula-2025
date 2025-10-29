from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_channel_message(group_name: str, message: dict):
    channel_layer_instance = get_channel_layer()
    async_to_sync(channel_layer_instance.group_send)(group_name, {
        'type': 'group.message',
        'content': message
    })
