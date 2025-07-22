# websocket/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import myapp.routing  # ✅ import your routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(  # ✅ must include this
        URLRouter(
            myapp.routing.websocket_urlpatterns  # ✅ your routes
        )
    ),
})
