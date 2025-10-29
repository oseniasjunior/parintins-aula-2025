from django.urls import path

from core import consumers

websocket_urlpatterns = [
    path('sale/', consumers.SaleConsumer.as_asgi())
]