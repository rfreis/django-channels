import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing

from app.settings.utils import *


SETTINGS_MODULE_PATH = get_env_var('SETTINGS_MODULE_PATH')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE_PATH)

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})