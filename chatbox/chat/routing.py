from . import consumers
from django.urls import path

websocket_urlpatterns=[
    path('ws/sc/<str:groupkoname>/',consumers.MySyncConsumer.as_asgi()),
    

    

]