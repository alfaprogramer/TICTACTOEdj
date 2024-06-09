import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path
from tictac.consumers import GameRoom

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TICTACTOE.settings')

# Initialize Django ASGI application early to ensure the AppRegistry is populated
django_asgi_app = get_asgi_application()

ws_patterns = [
    path('ws/game/<code>/', GameRoom.as_asgi())  # Ensure trailing slash
]

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(ws_patterns)
    ),
})
