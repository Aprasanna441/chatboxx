"""
ASGI config for dynamic_name project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import chat.routing
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dynamic_name.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':
    AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                    chat.routing.websocket_urlpatterns)
                    ))
})



